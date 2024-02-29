import gradio as gr
from pytube import YouTube
from faster_whisper import WhisperModel
from moviepy.editor import AudioFileClip, VideoFileClip







def video_text(input,model):
    video = VideoFileClip(input)
    audio = video.audio
    audio_path = "extracted_audio." + ".mp3"
    audio.write_audiofile(audio_path)
    video.close()
    seg=" "
    segments, info = model.transcribe((input))
    for segment in segments:
      seg +="%s" % (segment.text)
    return seg
    


