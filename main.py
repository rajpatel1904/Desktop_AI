import speech_recognition as s
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print('Pycharm')
    speak('Hello, I am Desktop A.I.')