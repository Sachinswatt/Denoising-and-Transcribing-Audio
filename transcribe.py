import whisper

print("Loading Whisper model...")

model = whisper.load_model("small")

print("Transcribing audio...")

result = model.transcribe(
    "war-intercept.wav",
    language="en",
    fp16=False
)

print("\n========== TRANSCRIPT ==========\n")
print(result["text"])

with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("\nTranscript saved to transcript.txt")