# Odev3-Merge

# 🗣️ Voice Assistant - Basic Speech Recognition in Python

This project is a simple voice assistant built using Python's `speech_recognition` and `pyttsx3` libraries. It listens to the user's voice through the microphone and responds based on the detected speech.

## 🎯 Features

- Recognizes basic speech using Google Web Speech API
- Responds with voice using `pyttsx3`
- Handles simple phrases like "hi" and "by"
- Error handling for unrecognized or failed voice input

## 🧠 How It Works

1. Uses `speech_recognition` to capture audio from your microphone.
2. Converts the audio to text using Google Speech API.
3. Depending on the detected phrase, the assistant responds:
   - "hi" → "Hi again!"
   - "by" → "By now!"
   - Anything else → "Hello"

## 🔧 Requirements

- Python 3.x
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- PyAudio (for microphone access)

You can install the dependencies using:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
