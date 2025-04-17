import gradio as gr
import whisperx
import torch
from kokoro_tts import KokoroTTS  # Assuming you have a Kokoro TTS wrapper
import tempfile
import os

def transcribe_audio(audio_file):
    model = whisperx.load_model("medium", device="cuda" if torch.cuda.is_available() else "cpu")
    audio = whisperx.load_audio(audio_file)
    result = model.transcribe(audio)
    return result["text"]

def generate_podcast(text):
    kokoro = KokoroTTS()
    audio_path = "output_podcast.wav"
    kokoro.synthesize(text, audio_path)
    return audio_path

def process_text_input(text):
    return generate_podcast(text)

def process_speech_input():
    return "Real-time speech processing not yet implemented"

def process_file_upload(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(file.read())
        temp_audio_path = temp_audio.name
    
    transcribed_text = transcribe_audio(temp_audio_path)
    os.remove(temp_audio_path)  # Clean up temporary file
    return generate_podcast(transcribed_text)

demo = gr.Interface(
    fn={
        "Text Input": process_text_input,
        "Speech Input": process_speech_input,
        "File Upload": process_file_upload
    },
    inputs=[
        gr.Textbox(label="Enter Podcast Text"),
        gr.Audio(source="microphone", type="filepath", label="Speak"),
        gr.File(label="Upload Audio File")
    ],
    outputs=gr.Audio(label="Generated Podcast"),
    title="Podcast Generator",
    description="Generate podcasts using Kokoro TTS from text, speech, or uploaded audio files."
)

demo.launch()
