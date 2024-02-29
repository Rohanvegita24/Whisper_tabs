import gradio as gr
from pytube import YouTube
from faster_whisper import WhisperModel
from moviepy.editor import AudioFileClip, VideoFileClip




final=[]

def  maudiottext (input,model):
   print(input)
   seg=" "
   segments, info = model.transcribe(input,language="en")
   for segment in segments:
     seg +="%s" % (segment.text)
   final.append(seg)
   output_string = ' '.join(final)
   return output_string



