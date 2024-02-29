from faster_whisper import WhisperModel
import gradio as gr



def audiototranslate(input,model):
  seg=" "
  segments, info = model.transcribe(input,task="translate",language="hi")
  for segment in segments:
    seg +="%s" % (segment.text)
  return seg