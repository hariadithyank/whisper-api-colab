!pip install -q openai-whisper gradio ffmpeg

import whisper
import gradio as gr

model = whisper.load_model("base")

def transcribe_audio(audio):
    result = model.transcribe(audio)
    return result["text"]

gr.Interface(fn=transcribe_audio, inputs="microphone", outputs="text").launch(share=True)
