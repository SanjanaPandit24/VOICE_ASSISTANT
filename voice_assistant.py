import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

# 1. Voice Setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 = Male, 1 = Female
engine.setProperty('rate', 175)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}")
        return query.lower()
    except:
        return "none"

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning Sir!")
    elif hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am your voice assistant. Tell me how can I help you?")

# 2. Main Program
if __name__ == "__main__":
    wish()
    while True:
        query = take_command()

        if query == "none":
            continue

        # Wikipedia Search
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except:
                speak("Not found on Wikipedia")

        # Open Websites
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif 'open github' in query:
            webbrowser.open("https://github.com")

        # Play on Youtube
        elif 'play' in query:
            song = query.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        # Time
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"It is {time}")

        # Date
        elif 'date' in query:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today is {date}")

        # Exit
        elif 'exit' in query or 'bye' in query or 'stop' in query:
            speak("Okay Sir, Have a good day. Bye!")
            break

        # Your Name
        elif 'your name' in query:
            speak("My name is JARVIS, your personal voice assistant.")