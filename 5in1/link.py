import gradio as gr
from pytube import YouTube
from faster_whisper import WhisperModel
from moviepy.editor import AudioFileClip, VideoFileClip



def yt_to_audio(video_path,model):
    yt = YouTube(video_path)
    yt_stream = yt.streams.filter(only_audio=False).first()
    audio_file_path = yt_stream.download(filename="temp_video")
    
    video = VideoFileClip(audio_file_path)
    audio = video.audio
    audio_path = "extracted_audio." + ".mp3"
    audio.write_audiofile(audio_path)
    video.close()
    seg=" "
    segments, info = model.transcribe((audio_path))
    for segment in segments:
      seg +="%s" % (segment.text)
    return seg


