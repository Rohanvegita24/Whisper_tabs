import whisper_timestamped as whisper
import gradio as gr 



def timestamp (input,model):

    audio = whisper.load_audio(input)

   

    result = whisper.transcribe(model, audio, language="en")

    import json
    final=json.dumps(result, indent = 2, ensure_ascii = False)
    return final

