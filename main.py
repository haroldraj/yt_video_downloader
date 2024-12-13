
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("url: ").strip()

yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download()