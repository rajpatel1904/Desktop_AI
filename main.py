import speech_recognition as s
import pyttsx3


def speak( text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeWord():
    r = s.Recognizer()
    with s.Microphone() as source:
        r.pause_threshold = 1
        a = r.listen(source)
        q = r.recognize_google(a, language='en-in')
        print(f'{q}')
        return q


if __name__ == '__main__':
    print('Pycharm')
    speak('Hello, I am Desktop A.I.')
    text = takeWord()
    speak(text)
