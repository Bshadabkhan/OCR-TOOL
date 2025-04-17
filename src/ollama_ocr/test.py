# import os
# import pytesseract
# import google.generativeai as genai
# import streamlit as st
# from PIL import Image
# from pdf2image import convert_from_bytes
# from reportlab.pdfgen import canvas
# from io import BytesIO
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # ✅ Load Google API Key Securely
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Ensure this is set in your environment variables
# if not GOOGLE_API_KEY:
#     st.error("Google API Key is missing! Set it as an environment variable: GOOGLE_API_KEY")
#     st.stop()

# genai.configure(api_key=GOOGLE_API_KEY)

# # ✅ Set Tesseract OCR Path (Update this for your system)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # ✅ Streamlit App Layout
# st.sidebar.write("👨OCR Tool")
# st.title("📝 OCR Chatbot")
# st.sidebar.write("Upload an image or PDF to extract text and get a response from Gemini AI.")

# uploaded_file = st.sidebar.file_uploader("Upload Image or PDF", type=["png", "jpg", "jpeg", "pdf"])

# # ✅ Sidebar for Custom User Prompt
# st.subheader("Customize Gemini Response")
# user_prompt = st.text_area("Enter your custom prompt:", "Summarize this text.")

# def extract_text_from_image(image):
#     """Extract text from an image using Tesseract OCR."""
#     try:
#         img = Image.open(image)
#         return pytesseract.image_to_string(img)
#     except Exception as e:
#         return f"Error processing image: {str(e)}"

# def extract_text_from_pdf(pdf_bytes):
#     """Extract text from a PDF using OCR."""
#     text = ""
#     try:
#         images = convert_from_bytes(pdf_bytes.read(), poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin")  # ✅ Update your Poppler path

#         for img in images:
#             text += pytesseract.image_to_string(img) + "\n"
#         return text if text.strip() else "No text detected in the PDF."
    
#     except Exception as e:
#         return f"Error processing PDF: {str(e)}"

# def gemini_chat_response(text, prompt):
#     """Generate a response using Google Gemini AI with a custom prompt."""
#     try:
#         model = genai.GenerativeModel("gemini-2.0-flash")  # ✅ Corrected model version
#         full_prompt = f"{prompt}\n\n{text}"
#         print(full_prompt)
#         response = model.generate_content(full_prompt)
#         return response.text if response else "Sorry, no response from Gemini."
    
#     except Exception as e:
#         return f"Error with Gemini API: {str(e)}"

# def gemini_feedback(response):
#     """Ask Gemini to evaluate its own response for quality feedback."""
#     try:
#         model = genai.GenerativeModel("gemini-2.0-flash")
#         feedback_prompt = f"Evaluate the quality of this response:\n\n{response}\n\nProvide constructive feedback."
#         feedback_response = model.generate_content(feedback_prompt)
#         print(feedback_response)
#         return feedback_response.text if feedback_response else "No feedback available."
    
#     except Exception as e:
#         return f"Error getting feedback from Gemini: {str(e)}"

# def generate_pdf(text):
#     """Generate a downloadable PDF from extracted text."""
#     buffer = BytesIO()
#     c = canvas.Canvas(buffer)
#     c.setFont("Helvetica", 12)
    
#     text_obj = c.beginText(100, 750)
#     text_obj.setFont("Helvetica", 12)
    
#     for line in text.split("\n"):
#         text_obj.textLine(line)
    
#     c.drawText(text_obj)
#     c.save()
    
#     buffer.seek(0)
#     return buffer

# if uploaded_file:
#     filename = uploaded_file.name.lower()
#     extracted_text = ""

#     if filename.endswith(("png", "jpg", "jpeg")):
#         extracted_text = extract_text_from_image(uploaded_file)
#     elif filename.endswith(".pdf"):
#         extracted_text = extract_text_from_pdf(uploaded_file)

#     if extracted_text.strip():
#         st.subheader("Extracted Text:")
#         st.text_area("OCR Result", extracted_text, height=200)

#         response = gemini_chat_response(extracted_text, user_prompt)
#         st.subheader("Gemini AI Response:")
#         st.write(response)

#         # Get feedback on Gemini's response
#         feedback = gemini_feedback(response)
#         st.subheader("Gemini's Feedback on the Response:")
#         st.write(feedback)

#         pdf_buffer = generate_pdf(extracted_text)
#         st.download_button(label="📄 Download Extracted Text as PDF", data=pdf_buffer, file_name="extracted_text.pdf", mime="application/pdf")
#     else:
#         st.error("No readable text found. Try another file.")




# import os
# import pytesseract
# import google.generativeai as genai
# import streamlit as st
# from PIL import Image
# from pdf2image import convert_from_bytes
# from reportlab.pdfgen import canvas
# from io import BytesIO
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # ✅ Load Google API Key Securely
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Ensure this is set in your environment variables
# if not GOOGLE_API_KEY:
#     st.error("Google API Key is missing! Set it as an environment variable: GOOGLE_API_KEY")
#     st.stop()

# genai.configure(api_key=GOOGLE_API_KEY)

# # ✅ Set Tesseract OCR Path (Update this for your system)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # ✅ Initialize session state for chat history if it doesn't exist
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # ✅ Streamlit App Layout
# st.sidebar.write("👨OCR Tool")
# st.title("📝 OCR Chatbot")
# st.sidebar.write("Upload an image or PDF to extract text and get a response.")

# uploaded_file = st.sidebar.file_uploader("Upload Image or PDF", type=["png", "jpg", "jpeg", "pdf"])

# # ✅ Add Clear Chat Button to sidebar
# if st.sidebar.button("🧹 Clear Chat History"):
#     st.session_state.chat_history = []
#     st.success("Chat history cleared!")



# user_prompt = st.chat_input("Enter your custom prompt:")

# def extract_text_from_image(image):
#     """Extract text from an image using Tesseract OCR."""
#     try:
#         img = Image.open(image)
#         return pytesseract.image_to_string(img)
#     except Exception as e:
#         return f"Error processing image: {str(e)}"

# def extract_text_from_pdf(pdf_bytes):
#     """Extract text from a PDF using OCR."""
#     text = ""
#     try:
#         images = convert_from_bytes(pdf_bytes.read(), poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin")  # ✅ Update your Poppler path

#         for img in images:
#             text += pytesseract.image_to_string(img) + "\n"
#         return text if text.strip() else "No text detected in the PDF."
    
#     except Exception as e:
#         return f"Error processing PDF: {str(e)}"

# def gemini_chat_response(text, prompt):
#     """Generate a response using Google Gemini AI with a custom prompt."""
#     try:
#         model = genai.GenerativeModel("gemini-2.0-flash")  # ✅ Corrected model version
#         full_prompt = f"{prompt}\n\n{text}"
#         print(full_prompt)
#         response = model.generate_content(full_prompt)
#         return response.text if response else "Sorry, no response from Gemini."
    
#     except Exception as e:
#         return f"Error with Gemini API: {str(e)}"

# def generate_pdf(text):
#     """Generate a downloadable PDF from extracted text."""
#     buffer = BytesIO()
#     c = canvas.Canvas(buffer)
#     c.setFont("Helvetica", 12)
    
#     text_obj = c.beginText(100, 750)
#     text_obj.setFont("Helvetica", 12)
    
#     for line in text.split("\n"):
#         text_obj.textLine(line)
    
#     c.drawText(text_obj)
#     c.save()
    
#     buffer.seek(0)
#     return buffer

# # ✅ Display chat history
# st.subheader("💬 Chat History")
# for i, chat_entry in enumerate(st.session_state.chat_history):
#     if chat_entry["type"] == "user":
#         st.write(f"👤 **User**: {chat_entry['content']}")
#     elif chat_entry["type"] == "system":
#         st.write(f"🖥️ **System**: {chat_entry['content']}")
#     elif chat_entry["type"] == "ai":
#         st.write(f"🤖 **AI**: {chat_entry['content']}")
    
#     # Add a separator between chat entries except for the last one
#     if i < len(st.session_state.chat_history) - 1:
#         st.markdown("---")

# if uploaded_file:
#     filename = uploaded_file.name.lower()
#     extracted_text = ""

#     if filename.endswith(("png", "jpg", "jpeg")):
#         extracted_text = extract_text_from_image(uploaded_file)
#     elif filename.endswith(".pdf"):
#         extracted_text = extract_text_from_pdf(uploaded_file)

#     if extracted_text.strip():
#         # ✅ Add system message to chat history about the file upload
#         st.session_state.chat_history.append({
#             "type": "system",
#             "content": f"File '{filename}' processed. Text extracted successfully."
#         })
        
#         st.subheader("Extracted Text:")
#         st.text_area("OCR Result", extracted_text, height=150)

#         # ✅ Add extracted text to chat history
#         st.session_state.chat_history.append({
#             "type": "user",
#             "content": f"[Extracted text from {filename}]: {extracted_text[:100]}..." if len(extracted_text) > 100 else extracted_text
#         })

#         # ✅ Only process with Gemini if user provided a prompt
#         if user_prompt:
#             response = gemini_chat_response(extracted_text, user_prompt)
#             st.subheader("Gemini AI Response:")
#             st.write(response)

#             # Add AI response to chat history
#             st.session_state.chat_history.append({
#                 "type": "ai",
#                 "content": response[:200] + "..." if len(response) > 200 else response
#             })


#         else:
#             # Inform user they need to provide a prompt
#             st.info("📝 Enter a prompt to get AI analysis of the extracted text.")

#         pdf_buffer = generate_pdf(extracted_text)
#         st.download_button(label="📄 Download Extracted Text as PDF", data=pdf_buffer, file_name="extracted_text.pdf", mime="application/pdf")
#     else:
#         error_msg = "No readable text found. Try another file."
#         st.error(error_msg)
        
#         # ✅ Add error message to chat history
#         st.session_state.chat_history.append({
#             "type": "system",
#             "content": f"Error: {error_msg}"
#         })

# # ✅ Handle direct user prompts without file upload
# if user_prompt and not uploaded_file:
#     # Add user prompt to chat history
#     st.session_state.chat_history.append({
#         "type": "user",
#         "content": user_prompt
#     })
    
#     response = gemini_chat_response("", user_prompt)
    
#     # Add AI response to chat history
#     st.session_state.chat_history.append({
#         "type": "ai",
#         "content": response
#     })
    
#     # Force a rerun to update the chat display
#     st.rerun()



# import os
# import pytesseract
# import google.generativeai as genai
# import streamlit as st
# from PIL import Image
# from pdf2image import convert_from_bytes
# from reportlab.pdfgen import canvas
# from io import BytesIO
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # ✅ Load Google API Key Securely
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Ensure this is set in your environment variables
# if not GOOGLE_API_KEY:
#     st.error("Google API Key is missing! Set it as an environment variable: GOOGLE_API_KEY")
#     st.stop()

# genai.configure(api_key=GOOGLE_API_KEY)

# # ✅ Set Tesseract OCR Path (Update this for your system)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # ✅ Initialize session state for chat history if it doesn't exist
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # ✅ Initialize session state for transformed prompt
# if "transformed_prompt" not in st.session_state:
#     st.session_state.transformed_prompt = ""

# if "original_prompt" not in st.session_state:
#     st.session_state.original_prompt = ""

# if "needs_processing" not in st.session_state:
#     st.session_state.needs_processing = False

# # ✅ Streamlit App Layout
# st.sidebar.write("👨OCR Tool")
# st.title("📝 OCR Chatbot")
# st.sidebar.write("Upload an image or PDF to extract text and get a response.")

# uploaded_file = st.sidebar.file_uploader("Upload Image or PDF", type=["png", "jpg", "jpeg", "pdf"])

# # ✅ Add Clear Chat Button to sidebar
# if st.sidebar.button("🧹 Clear Chat History"):
#     st.session_state.chat_history = []
#     st.success("Chat history cleared!")

# # Function to transform prompt
# def transform_prompt(input_prompt):
#     """Transform the user prompt into a more detailed and meaningful version."""
#     if not input_prompt:
#         return ""
    
#     try:
#         model = genai.GenerativeModel("gemini-2.0-flash")
#         system_prompt = """
#         Transform the following user prompt into a more detailed, professional and 
#         meaningful version that would help extract better information from OCR text. 
#         Return only the transformed prompt without explanations, prefixes or quotations.
#         """
        
#         full_prompt = f"{system_prompt}\n\nUser prompt: {input_prompt}"
#         response = model.generate_content(full_prompt)
#         return response.text if response else input_prompt
    
#     except Exception as e:
#         print(f"Error transforming prompt: {str(e)}")
#         return input_prompt  # Fallback to original prompt if transformation fails

# def extract_text_from_image(image):
#     """Extract text from an image using Tesseract OCR."""
#     try:
#         img = Image.open(image)
#         return pytesseract.image_to_string(img)
#     except Exception as e:
#         return f"Error processing image: {str(e)}"

# def extract_text_from_pdf(pdf_bytes):
#     """Extract text from a PDF using OCR."""
#     text = ""
#     try:
#         images = convert_from_bytes(pdf_bytes.read(), poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin")  # ✅ Update your Poppler path

#         for img in images:
#             text += pytesseract.image_to_string(img) + "\n"
#         return text if text.strip() else "No text detected in the PDF."
    
#     except Exception as e:
#         return f"Error processing PDF: {str(e)}"

# def gemini_chat_response(text, prompt):
#     """Generate a response using Google Gemini AI with a custom prompt."""
#     try:
#         model = genai.GenerativeModel("gemini-2.0-flash")  # ✅ Using correct model version
#         full_prompt = f"{prompt}\n\n{text}"
#         print(full_prompt)
#         response = model.generate_content(full_prompt)
#         return response.text if response else "Sorry, no response from Gemini."
    
#     except Exception as e:
#         return f"Error with Gemini API: {str(e)}"

# def generate_pdf(text):
#     """Generate a downloadable PDF from extracted text."""
#     buffer = BytesIO()
#     c = canvas.Canvas(buffer)
#     c.setFont("Helvetica", 12)
    
#     text_obj = c.beginText(100, 750)
#     text_obj.setFont("Helvetica", 12)
    
#     for line in text.split("\n"):
#         text_obj.textLine(line)
    
#     c.drawText(text_obj)
#     c.save()
    
#     buffer.seek(0)
#     return buffer

# # Create chat input without a callback
# user_prompt = st.chat_input("Enter your prompt:")

# # Handle the input when submitted
# if user_prompt:
#     # Store the original prompt
#     st.session_state.original_prompt = user_prompt
    
#     # Transform the prompt
#     transformed = transform_prompt(user_prompt)
#     st.session_state.transformed_prompt = transformed
    
#     # Flag that we need to process this prompt
#     st.session_state.needs_processing = True
    
#     # Force a rerun to update the UI with transformed prompt before processing
#     st.rerun()

# # Display transformed prompt if available
# if st.session_state.transformed_prompt:
#     st.info(f"📝 Transformed prompt: {st.session_state.transformed_prompt}")

# # Display chat history
# st.subheader("💬 Chat History")
# for i, chat_entry in enumerate(st.session_state.chat_history):
#     if chat_entry["type"] == "user":
#         st.write(f"👤 **User**: {chat_entry['content']}")
#     elif chat_entry["type"] == "system":
#         st.write(f"🖥️ **System**: {chat_entry['content']}")
#     elif chat_entry["type"] == "ai":
#         st.write(f"🤖 **AI**: {chat_entry['content']}")
    
#     # Add a separator between chat entries except for the last one
#     if i < len(st.session_state.chat_history) - 1:
#         st.markdown("---")

# if uploaded_file:
#     filename = uploaded_file.name.lower()
#     extracted_text = ""

#     if filename.endswith(("png", "jpg", "jpeg")):
#         extracted_text = extract_text_from_image(uploaded_file)
#     elif filename.endswith(".pdf"):
#         extracted_text = extract_text_from_pdf(uploaded_file)

#     if extracted_text.strip():
#         # ✅ Add system message to chat history about the file upload
#         st.session_state.chat_history.append({
#             "type": "system",
#             "content": f"File '{filename}' processed. Text extracted successfully."
#         })
        
#         st.subheader("Extracted Text:")
#         st.text_area("OCR Result", extracted_text, height=150)

#         # ✅ Add extracted text to chat history
#         st.session_state.chat_history.append({
#             "type": "user",
#             "content": f"[Extracted text from {filename}]: {extracted_text[:100]}..." if len(extracted_text) > 100 else extracted_text
#         })

#         # ✅ Use transformed prompt if available
#         active_prompt = st.session_state.transformed_prompt
        
#         # ✅ Only process with Gemini if user provided a prompt
#         if active_prompt:
#             response = gemini_chat_response(extracted_text, active_prompt)
#             st.subheader("Gemini AI Response:")
#             st.write(response)

#             # Add AI response to chat history
#             st.session_state.chat_history.append({
#                 "type": "ai",
#                 "content": response[:200] + "..." if len(response) > 200 else response
#             })
            
#             # Reset the transformed prompt after using it
#             st.session_state.transformed_prompt = ""
#             st.session_state.original_prompt = ""
#             st.session_state.needs_processing = False

#         else:
#             # Inform user they need to provide a prompt
#             st.info("📝 Enter a prompt to get AI analysis of the extracted text.")

#         pdf_buffer = generate_pdf(extracted_text)
#         st.download_button(label="📄 Download Extracted Text as PDF", data=pdf_buffer, file_name="extracted_text.pdf", mime="application/pdf")
#     else:
#         error_msg = "No readable text found. Try another file."
#         st.error(error_msg)
        
#         # ✅ Add error message to chat history
#         st.session_state.chat_history.append({
#             "type": "system",
#             "content": f"Error: {error_msg}"
#         })

# # ✅ Handle direct user prompts without file upload (after rerun)
# if st.session_state.needs_processing and st.session_state.transformed_prompt and not uploaded_file:
#     # Add both original and transformed prompts to chat history
#     st.session_state.chat_history.append({
#         "type": "user",
#         "content": f"Original: {st.session_state.original_prompt}\nTransformed: {st.session_state.transformed_prompt}"
#     })
    
#     response = gemini_chat_response("", st.session_state.transformed_prompt)
    
#     # Add AI response to chat history
#     st.session_state.chat_history.append({
#         "type": "ai",
#         "content": response
#     })
    
#     # Reset prompts after processing
#     st.session_state.transformed_prompt = ""
#     st.session_state.original_prompt = ""
#     st.session_state.needs_processing = False
    
#     # Force a rerun to update the chat display
#     st.rerun()



# import os
# import pytesseract
# import google.generativeai as genai
# import streamlit as st
# from PIL import Image
# from pdf2image import convert_from_bytes
# from reportlab.pdfgen import canvas
# from io import BytesIO
# from dotenv import load_dotenv
# from datetime import datetime  # Optional for timestamps

# # Load environment variables
# load_dotenv()

# # ✅ Load Google API Key Securely
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# if not GOOGLE_API_KEY:
#     st.error("Google API Key is missing! Set it as an environment variable: GOOGLE_API_KEY")
#     st.stop()

# genai.configure(api_key=GOOGLE_API_KEY)

# # ✅ Set Tesseract OCR Path
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # ✅ Initialize session states
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if "transformed_prompt" not in st.session_state:
#     st.session_state.transformed_prompt = ""

# if "original_prompt" not in st.session_state:
#     st.session_state.original_prompt = ""

# if "needs_processing" not in st.session_state:
#     st.session_state.needs_processing = False

# # ✅ Streamlit App Layout
# st.sidebar.write("👨OCR Tool")
# st.title("📝 OCR Chatbot")
# st.sidebar.write("Upload an image or PDF to extract text and get a response.")

# uploaded_file = st.sidebar.file_uploader("Upload Image or PDF", type=["png", "jpg", "jpeg", "pdf"])

# # ✅ Add Clear Chat Button
# if st.sidebar.button("🧹 Clear Chat History"):
#     st.session_state.chat_history = []
#     st.success("Chat history cleared!")

# # ✅ Transform prompt function
# def transform_prompt(input_prompt):
#     if not input_prompt:
#         return ""
#     try:
#         model = genai.GenerativeModel("gemini-2.0-flash")
#         system_prompt = """
#         Transform the following user prompt into a more detailed, professional and 
#         meaningful version that would help extract better information from OCR text. 
#         Return only the transformed prompt without explanations, prefixes or quotations.
#         """
#         full_prompt = f"{system_prompt}\n\nUser prompt: {input_prompt}"
#         response = model.generate_content(full_prompt)
#         return response.text if response else input_prompt
#     except Exception as e:
#         st.exception(f"Error transforming prompt: {str(e)}")
#         return input_prompt

# # ✅ OCR functions
# def extract_text_from_image(image):
#     try:
#         img = Image.open(image)
#         return pytesseract.image_to_string(img)
#     except Exception as e:
#         st.exception(f"Error processing image: {str(e)}")
#         return ""

# def extract_text_from_pdf(pdf_bytes):
#     text = ""
#     try:
#         images = convert_from_bytes(pdf_bytes.read(), poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin")
#         for img in images:
#             text += pytesseract.image_to_string(img) + "\n"
#         return text if text.strip() else "No text detected in the PDF."
#     except Exception as e:
#         st.exception(f"Error processing PDF: {str(e)}")
#         return ""

# # ✅ Gemini Chat
# def gemini_chat_response(text, prompt):
#     try:
#         model = genai.GenerativeModel("gemini-2.0-flash")
#         full_prompt = f"{prompt}\n\n{text}"
#         response = model.generate_content(full_prompt)
#         return response.text if response else "Sorry, no response from Gemini."
#     except Exception as e:
#         st.exception(f"Error with Gemini API: {str(e)}")
#         return "Error generating response."

# # ✅ PDF download
# def generate_pdf(text):
#     buffer = BytesIO()
#     c = canvas.Canvas(buffer)
#     c.setFont("Helvetica", 12)
#     text_obj = c.beginText(100, 750)
#     text_obj.setFont("Helvetica", 12)
#     for line in text.split("\n"):
#         text_obj.textLine(line)
#     c.drawText(text_obj)
#     c.save()
#     buffer.seek(0)
#     return buffer

# # ✅ Chat Input (only active after upload)
# if uploaded_file:
#     user_prompt = st.chat_input("Enter your prompt:")
# else:
#     st.chat_input("Upload a file first to begin.", disabled=True)
#     user_prompt = None

# # ✅ Handle user prompt input
# if user_prompt:
#     st.session_state.original_prompt = user_prompt
#     transformed = transform_prompt(user_prompt)
#     st.session_state.transformed_prompt = transformed
#     st.session_state.needs_processing = True
#     st.rerun()

# # ✅ Show original and transformed prompt side-by-side
# if st.session_state.original_prompt and st.session_state.transformed_prompt:
#     st.markdown("### ✨ Prompt Transformation")
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("**📝 Original Prompt**")
#         st.code(st.session_state.original_prompt, language="text")
#     with col2:
#         st.markdown("**🔧 Transformed Prompt**")
#         st.code(st.session_state.transformed_prompt, language="text")

# # ✅ Show Chat History
# st.subheader("💬 Chat History")
# for i, chat_entry in enumerate(st.session_state.chat_history):
#     if chat_entry["type"] == "user":
#         st.write(f"👤 **User**: {chat_entry['content']}")
#     elif chat_entry["type"] == "system":
#         st.write(f"🖥️ **System**: {chat_entry['content']}")
#     elif chat_entry["type"] == "ai":
#         st.write(f"🤖 **AI**: {chat_entry['content']}")
#     if i < len(st.session_state.chat_history) - 1:
#         st.markdown("---")

# # ✅ File processing
# if uploaded_file:
#     filename = uploaded_file.name.lower()
#     extracted_text = ""

#     if filename.endswith(("png", "jpg", "jpeg")):
#         extracted_text = extract_text_from_image(uploaded_file)
#     elif filename.endswith(".pdf"):
#         extracted_text = extract_text_from_pdf(uploaded_file)

#     if extracted_text.strip():
#         st.session_state.chat_history.append({
#             "type": "system",
#             "content": f"File '{filename}' processed. Text extracted successfully."
#         })

#         st.subheader("Extracted Text:")
#         with st.expander("🔍 View Full Extracted Text"):
#             st.text_area("OCR Result", extracted_text, height=300)

#         st.session_state.chat_history.append({
#             "type": "user",
#             "content": f"[Extracted text from {filename}]: {extracted_text[:100]}..." if len(extracted_text) > 100 else extracted_text
#         })

#         active_prompt = st.session_state.transformed_prompt

#         if active_prompt:
#             response = gemini_chat_response(extracted_text, active_prompt)
#             st.subheader("Gemini AI Response:")
#             st.write(response)

#             st.session_state.chat_history.append({
#                 "type": "ai",
#                 "content": response[:200] + "..." if len(response) > 200 else response
#             })

#             st.session_state.transformed_prompt = ""
#             st.session_state.original_prompt = ""
#             st.session_state.needs_processing = False
#         else:
#             st.info("📝 Enter a prompt to get AI analysis of the extracted text.")

#         pdf_buffer = generate_pdf(extracted_text)
#         st.download_button(label="📄 Download Extracted Text as PDF", data=pdf_buffer, file_name="extracted_text.pdf", mime="application/pdf")
#     else:
#         st.error("No readable text found. Try another file.")
#         st.session_state.chat_history.append({
#             "type": "system",
#             "content": "Error: No readable text found in file."
#         })

# # ✅ Handle prompt without upload
# if st.session_state.needs_processing and st.session_state.transformed_prompt and not uploaded_file:
#     st.session_state.chat_history.append({
#         "type": "user",
#         "content": f"Original: {st.session_state.original_prompt}\nTransformed: {st.session_state.transformed_prompt}"
#         # "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Optional
#     })

#     response = gemini_chat_response("", st.session_state.transformed_prompt)
#     st.session_state.chat_history.append({
#         "type": "ai",
#         "content": response
#     })

#     st.session_state.transformed_prompt = ""
#     st.session_state.original_prompt = ""
#     st.session_state.needs_processing = False
#     st.rerun()


import os
import pytesseract
import google.generativeai as genai
import streamlit as st
from PIL import Image
from pdf2image import convert_from_bytes
from reportlab.pdfgen import canvas
from io import BytesIO
from dotenv import load_dotenv

st.set_page_config(
    page_title="Multi-Document OCR Assistant",  # This will be your tab name
    page_icon="📝",  # Optional: adds an icon to your tab
    layout="wide",  # Optional: makes the layout wider
    initial_sidebar_state="expanded"  # Optional: starts with sidebar open
)

# Load environment variables
load_dotenv()

# Load Google API Key Securely
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Google API Key is missing! Set it as an environment variable: GOOGLE_API_KEY")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Set Tesseract OCR Path (Update this for your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "transformed_prompt" not in st.session_state:
    st.session_state.transformed_prompt = ""

if "original_prompt" not in st.session_state:
    st.session_state.original_prompt = ""

if "needs_processing" not in st.session_state:
    st.session_state.needs_processing = False

if "documents" not in st.session_state:
    st.session_state.documents = {}  # {filename: extracted_text}

if "selected_docs" not in st.session_state:
    st.session_state.selected_docs = {}

# Sidebar & Title
st.sidebar.write("👨 OCR Multi-Document Tool")
st.title("📝 Multi-Document OCR Chatbot")
st.sidebar.write("Upload images or PDFs to extract text and get responses.")

# File uploader widget
uploaded_files = st.sidebar.file_uploader("Upload Images or PDFs",
                                           type=["png", "jpg", "jpeg", "pdf"],
                                           accept_multiple_files=True)

# Clear chat and documents buttons
if st.sidebar.button("🧹 Clear Chat History"):
    st.session_state.chat_history = []
    st.success("Chat history cleared!")

def transform_prompt(input_prompt):
    if not input_prompt:
        return ""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        full_prompt = f"User prompt: {input_prompt}"
        response = model.generate_content(full_prompt)
        return response.text if response else input_prompt
    except Exception as e:
        print(f"Error transforming prompt: {str(e)}")
        return input_prompt

def extract_text_from_image(image):
    try:
        img = Image.open(image)
        return pytesseract.image_to_string(img)
    except Exception as e:
        return f"Error processing image: {str(e)}"

def extract_text_from_pdf(pdf_bytes):
    text = ""
    try:
        images = convert_from_bytes(pdf_bytes.read(), poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin")
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"
        return text if text.strip() else "No text detected in the PDF."
    except Exception as e:
        return f"Error processing PDF: {str(e)}"

def gemini_chat_response(text, prompt, is_comparison=False):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        if is_comparison:
            full_prompt = f"Compare and contrast the following documents:\n\n{text}\n\nPrompt: {prompt}"
        else:
            full_prompt = f"{prompt}\n\n{text}"
        response = model.generate_content(full_prompt)
        return response.text if response else "Sorry, no response from Gemini."
    except Exception as e:
        return f"Error with Gemini API: {str(e)}"

def generate_pdf(text):
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

# Process uploaded files
if uploaded_files:
    for uploaded_file in uploaded_files:
        filename = uploaded_file.name
        if filename in st.session_state.documents:
            continue
        extracted_text = ""
        if filename.lower().endswith(("png", "jpg", "jpeg")):
            extracted_text = extract_text_from_image(uploaded_file)
        elif filename.lower().endswith(".pdf"):
            extracted_text = extract_text_from_pdf(uploaded_file)
        if extracted_text.strip():
            st.session_state.documents[filename] = extracted_text
            st.session_state.chat_history.append({
                "type": "system",
                "content": f"File '{filename}' processed. Text extracted successfully."
            })
        else:
            warning = f"No readable text found in '{filename}'. Try another file."
            st.warning(warning)
            st.session_state.chat_history.append({
                "type": "system",
                "content": f"Warning: {warning}"
            })

# Document selection UI
if st.session_state.documents:
    st.sidebar.subheader("Available Documents")
    selected_docs = {}
    for doc_name in st.session_state.documents.keys():
        selected = st.sidebar.checkbox(f"{doc_name}", key=f"select_{doc_name}")
        selected_docs[doc_name] = selected
    st.session_state.selected_docs = selected_docs

    # Retrieve compare mode checkbox value without assigning it to session_state
    compare_mode = st.sidebar.checkbox("Compare selected documents", key="compare_mode")

    st.subheader("Selected Document Contents:")
    any_selected = any(selected_docs.values())
    if any_selected:
        for doc_name, is_selected in selected_docs.items():
            if is_selected:
                with st.expander(f"📄 {doc_name}"):
                    st.text_area(f"Content of {doc_name}",
                                 st.session_state.documents[doc_name],
                                 height=150,
                                 key=f"content_{doc_name}")
    else:
        st.info("Select one or more documents from the sidebar to view their contents.")
else:
    compare_mode = False  # Ensure compare_mode is defined when no documents exist

# User input
user_prompt = st.chat_input("Enter your prompt:")

if user_prompt:
    st.session_state.original_prompt = user_prompt
    st.session_state.transformed_prompt = transform_prompt(user_prompt)
    st.session_state.needs_processing = True
    st.rerun()

if st.session_state.transformed_prompt:
    st.info(f"📝 Transformed prompt: {st.session_state.transformed_prompt}")

# Chat History Display
st.subheader("💬 Chat History")
for i, entry in enumerate(st.session_state.chat_history):
    if entry["type"] == "user":
        st.write(f"👤 **User**: {entry['content']}")
    elif entry["type"] == "system":
        st.write(f"🖥️ **System**: {entry['content']}")
    elif entry["type"] == "ai":
        st.write(f"🤖 **AI**: {entry['content']}")
    if i < len(st.session_state.chat_history) - 1:
        st.markdown("---")

# Document + Prompt Processing
if st.session_state.needs_processing and st.session_state.transformed_prompt:
    selected_doc_names = [name for name, selected in st.session_state.selected_docs.items() if selected]
    if selected_doc_names:
        st.session_state.chat_history.append({
            "type": "user",
            "content": f"Prompt: {st.session_state.original_prompt}"
        })
        if compare_mode and len(selected_doc_names) > 1:
            combined = []
            for i, doc_name in enumerate(selected_doc_names):
                combined.append(f"Document {i+1} ({doc_name}):\n{st.session_state.documents[doc_name]}")
            full_text = "\n\n---\n\n".join(combined)
            response = gemini_chat_response(full_text, st.session_state.transformed_prompt, is_comparison=True)
            st.session_state.chat_history.append({
                "type": "system",
                "content": f"Comparing documents: {', '.join(selected_doc_names)}"
            })
            st.session_state.chat_history.append({
                "type": "ai",
                "content": response
            })
        else:
            for doc_name in selected_doc_names:
                doc_text = st.session_state.documents[doc_name]
                st.session_state.chat_history.append({
                    "type": "system",
                    "content": f"Processing document: {doc_name}"
                })
                response = gemini_chat_response(doc_text, st.session_state.transformed_prompt)
                st.session_state.chat_history.append({
                    "type": "ai",
                    "content": response
                })
    else:
        st.session_state.chat_history.append({
            "type": "user",
            "content": st.session_state.original_prompt
        })
        if st.session_state.documents:
            st.session_state.chat_history.append({
                "type": "system",
                "content": "Please select one or more documents from the sidebar to process your query."
            })
        else:
            response = gemini_chat_response("", st.session_state.transformed_prompt)
            st.session_state.chat_history.append({
                "type": "ai",
                "content": response
            })

    st.session_state.transformed_prompt = ""
    st.session_state.original_prompt = ""
    st.session_state.needs_processing = False
    st.rerun()

# Download PDFs option
if st.session_state.documents:
    st.subheader("Download Options")
    for doc_name, content in st.session_state.documents.items():
        pdf_buffer = generate_pdf(content)
        st.download_button(
            label=f"📄 Download {doc_name} as PDF",
            data=pdf_buffer,
            file_name=f"{os.path.splitext(doc_name)[0]}_extracted.pdf",
            mime="application/pdf",
            key=f"download_{doc_name}"
        )

# Optional Debug Helpers (uncomment if needed)
# st.sidebar.write("DEBUG selected_docs:", st.session_state.selected_docs)
# st.sidebar.write("DEBUG compare_mode:", compare_mode)
