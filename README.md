# Denoising and Transcribing Intercepted Audio

## 📌 Overview

This project is part of a digital/audio forensics challenge focused on analyzing an intercepted audio recording.

The objective of the challenge was to process an intercepted WAV audio file, improve its speech intelligibility, and convert the spoken content into machine-readable text using an automatic speech recognition model.

The workflow was implemented using **Python, Visual Studio Code, and OpenAI Whisper**.

---

## 🎯 Objectives

The main objectives of this challenge were:

- Preserve the original intercepted audio.
- Inspect the audio recording.
- Reduce unwanted background noise.
- Improve speech intelligibility.
- Transcribe the speech into text.
- Save the generated transcript for further analysis.
- Document the complete analysis process.

---

## 🛠️ Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Audio processing and automation |
| Visual Studio Code | Development environment |
| OpenAI Whisper | Speech-to-text transcription |
| Whisper Small Model | Automatic speech recognition |
| Python Virtual Environment | Dependency isolation |
| WAV / PCM | Input audio format |

---

## 📂 Project Structure

```text
Challenge_3_Audio/
│
├── .venv/
│
├── war-intercept.wav
│
├── transcribe.py
│
├── transcript.txt
│
└── README.md
