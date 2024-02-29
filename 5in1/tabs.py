from pytube import YouTube
from faster_whisper import WhisperModel
from moviepy.editor import AudioFileClip, VideoFileClip
from microphonetoaudioL import microphonetotext
from audiototext import auditotex
from mictoaudio import maudiottext
from videototext import video_text
from link import yt_to_audio
from Trans import audiototranslate
from down import texTS
import gradio as gr

model = WhisperModel("large-v2")
def tab1 (input):
    return microphonetotext(input,model)
def tab2 (input):
    return auditotex(input,model)
def tab3 (input):
    return maudiottext(input,model)
def tab4 (input):
    return video_text(input,model)
def tab5 (input):
    return yt_to_audio(input,model)
def tab6 (input):
    return audiototranslate(input,model)


                           

with gr.Blocks() as trail:
   
   with gr.Tab("Microphone to audio"):
      
      gr.Interface(fn=tab1,inputs=[gr.Audio(type="filepath",streaming=True)],outputs="text",title="Welcome to audio tabs bro!",description="tell something to whisper",live=True)

        
   with gr.Tab("youtube to audio"):
    
        gr.Interface(
    fn=tab5,inputs="textbox",outputs="text",
    examples=["https://www.youtube.com/watch?v=mCgBQFhQGf0&t=203s"],
    title="YouTube Video to Audio Converter",
    description="Enter a YouTube video link to convert it into an audio MP3 file.",
    allow_flagging=False)
      
   with gr.Tab("Audio file to transcrib"):
      
      gr.Interface(fn=tab2,inputs=[gr.Audio(sources="upload",type="filepath")],examples=["/home/team2/Rohan/5in1/Md.wav","/home/team2/Rohan/5in1/ISRO.mp3"],outputs="text",title="Audio to Transcript",description="tell something to whisper")

   with gr.Tab("Microphone to transcript"):
    
        gr.Interface(fn=tab3,inputs=[gr.Audio(sources="microphone",type="filepath")],outputs="text",title="Microphone to Transcript",description="Talk in the mic bro")

   with gr.Tab("video file to transcription"):
        gr.Interface(fn=tab4,inputs=gr.Video(),outputs="text",examples=["https://www.youtube.com/watch?v=EMUxukvWmIg","https://www.youtube.com/watch?v=i74SNAdtoY8"],title="Video to Audio Converter",description="Extract audio from a video file ")
    
   with gr.Tab("Audio to translate"):
    
        gr.Interface(fn=tab6,inputs=[gr.Audio(type="filepath",)],outputs="text",examples=["/home/team2/Rohan/5in1/M.mp3"],title="Microphone to Transcript",description="Talk in the mic bro")

   with gr.Tab("Text to Voice "):
    
        gr.Interface(fn=texTS,outputs="audio",inputs="text",examples=["Hello this is the whisper model , that convert text to voice "],title="Microphone to Transcript",description="Talk in the mic bro")
   
trail.launch(share=True)

