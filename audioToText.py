import whisper


model = whisper.load_model("base")
audio = "Audio/audio2.mp4"
result = model.transcribe(audio)


with open("transcription.txt", "w", encoding="utf-8") as txt:
    txt.write(result["text"])
