import os
from core.Text import colorText
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

####################### SYSTEM SOUND AND MICROPHONE SETTINGS #####################

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


os.system("cls")

# ASCII file
f = open("assets/Logo.txt", "r")
ascii = "".join(f.readlines())
print(colorText(ascii))

######################## SOME INITIAL FUNCTIONS ####################################


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alexa Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query


# wishMe()


while True:
    # query = takeCommand().lower()
    query = input("Type command: ")

    # Logic for executing tasks based on query

    if "wikipedia" in query:  # QUERY--> dinosaur wikipedia

        speak(f"Searching {query} on Wikipedia...")
        try:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except Exception as e:
            print("An error occured: ", e)

    elif (
        "open youtube" in query
        or "open google" in query
        or "open stackoverflow" in query
        or "open github" in query
    ):
        # QUERY--> open youtube etc etc

        from modules.browser import web

        web(query)
