#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr

recognizer = sr.Recognizer()

# We need to process audio files mp3, or videos mp4/avi... and extract the audio from it
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Could not request results from Google Speech Recognition service")
except Exception as e:
    print("Error: " + str(e))
