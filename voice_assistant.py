import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Say something (like 'Hi' or 'By'): ")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
    if "hi" in text.lower():
        print("Hi again!")
        engine.say("Hi again!")
        engine.runAndWait()
    elif "by" in text.lower():
        print("By now!")
        engine.say("By now!")
        engine.runAndWait()
    else:
        print("Hello")
        engine.say("Hello")
        engine.runAndWait()
except sr.UnknownValueError:
    print("Sorry, I couldnt understand what you said.")
    engine.say("Sorry, I couldnt understand.")
    engine.runAndWait()
except sr.RequestError:
    print("Sorry, there is a problem with the service.")
    engine.say("Service error.")
    engine.runAndWait()