import gradio as gr
from faster_whisper import WhisperModel



model = WhisperModel("large-v2")

previous_transcription = ""  # Initialize previous transcription

def stream(input_audio):
    global previous_transcription
    segments, info = model.transcribe(input_audio, language="en")
    transcriptions = []
    for segment in segments:
        transcriptions.append(segment.text)
    transcription = " ".join(transcriptions).strip()
    previous_transcription += " " + transcription
    return previous_transcription

iface = gr.Interface(fn=stream,
                     inputs=[gr.Audio(type="filepath", streaming=True)],
                     outputs="text",
                     title="Audio Transcription App",
                     description="Upload an audio file and hit the 'Submit' button",
                     live=True)

iface.launch()
