from pytube import YouTube

# Replace 'VIDEO_URL' with the URL of the YouTube video you want to download
video_url = input("Enter the url")

# Create a YouTube object
yt = YouTube(video_url)

# Select the stream with the audio you want (e.g., highest quality audio stream)
audio_stream = yt.streams.filter(only_audio=True).first()

# Set the output path and file name for the downloaded audio
output_path = './Audio'
audio_file = audio_stream.download(output_path=output_path)

print(f"Downloaded: {audio_file}")
