
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from news import speak_news
from ai import askAI




def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")

    elif "open github" in c.lower():
        webbrowser.open("https://github.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        headlines = speak_news()
        speak("Here are the top headlines")

        for headline in headlines:
            speak(headline)

    else:
        response = askAI(c)
        speak(response)


if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        r = sr.Recognizer()

        print("recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes boss")

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=10)

                command = r.recognize_google(audio)

                processCommand(command)

        except Exception:
            continue
