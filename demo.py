import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis, Sir. How may I assist you today?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again, please...")
        return "None"
    return query


def openWebsite(website_url):
    webbrowser.open(website_url)


def openApplication(application_path):
    os.startfile(application_path)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pssingh050205@gmail.com', 'virat@018')
    server.sendmail('pssingh050205@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            openWebsite("https://www.youtube.com/")

        elif 'open google' in query:
            openWebsite("https://www.google.com/")

        elif 'open stackoverflow' in query:
            openWebsite("https://stackoverflow.com/")

        elif 'open whatsapp' in query:
            openApplication("C:\Users\Dell\OneDrive\Desktop\WhatsApp.lnk")

        elif 'play music' in query:
            music_dir = 'pass'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'send email to partha' in query:
            try:
                speak("What should I say in the email?")
                content = takeCommand()
                to = "2201020101@cgu-odisha.ac.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send this email.")

        elif 'thank you' in query:
            speak("You're welcome, sir. How can I further assist you?")

        elif 'may I audiable' in query:
            speak("Yes, sir! You can give me orders.")

        elif 'stop' in query:
            speak("Goodbye!")
            break

        else:
            print("Query not recognized")
            speak("Please give me a valid command, sir.")
