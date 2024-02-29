import gradio as gr
from pytube import YouTube
from faster_whisper import WhisperModel
from moviepy.editor import AudioFileClip, VideoFileClip

model = WhisperModel("medium")

def yt_to_audio(video_path):
    yt = YouTube(video_path)
    yt_stream = yt.streams.filter(only_audio=False).first()
    audio_file_path = yt_stream.download(filename="temp_video")
       
    video = VideoFileClip(audio_file_path)
    audio = video.audio
    audio_path = "extracted_audio." + ".mp3"
    audio.write_audiofile(audio_path)
    video.close()
    return audiototext (audio_path)

def audiototext(input):
  seg=" "
  segments, info = model.transcribe((input))
  for segment in segments:
    seg +="%s" % (segment.text)
  return seg

def video_text(video_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio_path = "extracted_audio." + ".mp3"
    audio.write_audiofile(audio_path)
    video.close()
    return audiototext(audio_path)




with gr.Blocks() as trail:
   
   with gr.Tab("Microphone to audio"):
      
      gr.Interface(fn=audiototext,inputs=[gr.Audio(type="filepath",streaming=True)],outputs="text",title="FasterWhisper",description="tell something to whisper",live=True)

        
   with gr.Tab("youtube to audio"):
    
        gr.Interface(
    fn=yt_to_audio,inputs="textbox",outputs="text",
    title="YouTube Video to Audio Converter",
    description="Enter a YouTube video link to convert it into an audio MP3 file.",
    allow_flagging=False)
      
   with gr.Tab("Audio file to transcrib"):
      
      gr.Interface(fn=audiototext,inputs=[gr.Audio(sources="upload",type="filepath")],outputs="text",title="Audio to Transcript",description="tell something to whisper",live=True)

   with gr.Tab("Microphone to transcript"):
    
        gr.Interface(fn=audiototext,inputs=[gr.Audio(sources="microphone",type="filepath")],outputs="text",title="Microphone to Transcript",description="Talk in the mic bro",live=True)

   with gr.Tab("video file to transcription"):
       gr.Interface(fn=video_text,inputs=gr.Video(),outputs="text",title="Video to Audio Converter",description="Extract audio from a video file ")
   
trail.launch()

   