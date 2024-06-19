from pytube import YouTube

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(output_path)
    return stream.default_filename

# Example usage
video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
output_path = './videos'
filename = download_youtube_video(video_url, output_path)
print(f'Downloaded video as {filename}')
