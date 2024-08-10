import os
from yt_dlp import YoutubeDL

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['filename']} - {d['_percent_str']} completed, {d['_eta_str']} remaining.")
    elif d['status'] == 'finished':
        print(f"Download finished: {d['filename']} - {d['_total_bytes_str']} total size.")

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
folder_name = "YoutubeDownloader"
path = os.path.join(desktop_path, folder_name)

if not os.path.exists(path):
    os.makedirs(path)
    print(f"Created {folder_name} folder at: {path}")

url = input("Enter video URL: ")

ydl_opts = {
    'outtmpl': f'{path}/%(title)s.%(ext)s',
    'format': 'best',
    'progress_hooks': [progress_hook],
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
