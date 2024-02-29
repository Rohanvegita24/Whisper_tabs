import gradio as gr
from pytube import YouTube
from faster_whisper import WhisperModel
from moviepy.editor import AudioFileClip, VideoFileClip





def auditotex(input,model):
  seg=" "
  segments, info = model.transcribe((input))
  for segment in segments:
    seg +="%s" % (segment.text)
  return seg

iface=gr.Interface(
fn=auditotex,
inputs=[gr.Audio(sources="upload",type="filepath")],
outputs="text",title="Audio to Transcript",
description="tell something to whisper",live=True)
