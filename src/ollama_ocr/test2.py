import os
import pytesseract
import google.generativeai as genai
import streamlit as st
import pdfplumber
import cv2
import numpy as np
from PIL import Image, UnidentifiedImageError
from pdf2image import convert_from_bytes
from reportlab.pdfgen import canvas
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ✅ Load Google API Key Securely
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Google API Key is missing! Set it as an environment variable: GOOGLE_API_KEY")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Set Tesseract OCR Path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ✅ Streamlit App Layout
st.sidebar.write("👨OCR Tool")
st.title("📝 Enhanced OCR Chatbot")
st.write("Upload an image or PDF to extract text with improved accuracy and get a response from Gemini AI.")

uploaded_file = st.file_uploader("Upload Image or PDF", type=["png", "jpg", "jpeg", "pdf"])

# ✅ Sidebar for Custom User Prompt
st.sidebar.subheader("Customize Gemini Response")
user_prompt = st.sidebar.text_area("Enter your custom prompt:", "Summarize this text.")

def preprocess_image(image):
    """Preprocess image for better OCR accuracy."""
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return Image.fromarray(img)

def extract_text_from_image(image):
    """Extract text from an image using Tesseract OCR with preprocessing."""
    try:
        img = preprocess_image(image)
        return pytesseract.image_to_string(img, config="--psm 6")
    except Exception as e:
        return f"Error processing image: {str(e)}"

def extract_text_from_pdf(pdf_bytes):
    """Extract text from a PDF using OCR with robust image handling."""
    text = ""
    try:
        with pdfplumber.open(pdf_bytes) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
                # Loop over any images on the page
                for img_obj in page.images:
                    try:
                        image_data = img_obj["stream"].get_data()
                        # Attempt 1: Try opening with PIL directly
                        try:
                            image = Image.open(BytesIO(image_data)).convert("RGB")
                        except UnidentifiedImageError:
                            # Attempt 2: Use OpenCV to decode the image
                            nparr = np.frombuffer(image_data, np.uint8)
                            img_cv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                            if img_cv is not None:
                                image = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
                            else:
                                # Attempt 3: Use PIL.Image.frombytes with known width and height
                                try:
                                    w, h = int(img_obj["width"]), int(img_obj["height"])
                                    image = Image.frombytes("RGB", (w, h), image_data)
                                except Exception as e:
                                    st.warning(f"Fallback: could not decode image using frombytes: {str(e)}")
                                    continue
                        # Extract OCR text from the decoded image
                        text += "\n" + extract_text_from_image(image)
                    except Exception as e:
                        st.warning(f"Skipping an image due to processing error: {str(e)}")
        
        if not text.strip():
            # Fallback: Convert PDF pages to images and apply OCR
            images = convert_from_bytes(pdf_bytes.read(), poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin")
            for img in images:
                text += pytesseract.image_to_string(img) + "\n"
        
        return text if text.strip() else "No text detected in the PDF."
    except Exception as e:
        return f"Error processing PDF: {str(e)}"


def gemini_chat_response(text, prompt):
    """Generate a response using Google Gemini AI with a custom prompt."""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        full_prompt = f"{prompt}\n\n{text}"
        response = model.generate_content(full_prompt)
        return response.text if response else "Sorry, no response from Gemini."
    except Exception as e:
        return f"Error with Gemini API: {str(e)}"

def generate_pdf(text):
    """Generate a downloadable PDF from extracted text."""
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.setFont("Helvetica", 12)
    
    text_obj = c.beginText(100, 750)
    text_obj.setFont("Helvetica", 12)
    
    for line in text.split("\n"):
        text_obj.textLine(line)
    
    c.drawText(text_obj)
    c.save()
    
    buffer.seek(0)
    return buffer

if uploaded_file:
    filename = uploaded_file.name.lower()
    extracted_text = ""

    if filename.endswith(("png", "jpg", "jpeg")):
        extracted_text = extract_text_from_image(Image.open(uploaded_file))
    elif filename.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(uploaded_file)

    if extracted_text.strip():
        st.subheader("Extracted Text:")
        st.text_area("OCR Result", extracted_text, height=200)

        response = gemini_chat_response(extracted_text, user_prompt)
        st.subheader("Gemini AI Response:")
        st.write(response)

        pdf_buffer = generate_pdf(extracted_text)
        st.download_button(label="📄 Download Extracted Text as PDF", data=pdf_buffer, file_name="extracted_text.pdf", mime="application/pdf")
    else:
        st.error("No readable text found. Try another file.")
