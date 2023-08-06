import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language = 'en-US')
print('You said: ')
input()
