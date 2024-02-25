from time import process_time_ns
import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import platform
import psutil
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


video_directories = {
    "movies": "D:\\documents\\videos\\Movies",
    "videos": "D:\\documents\\videos",
    "The Wheel of Time S01": "D:\\documents\\videos\\Movies\\The Wheel of Time S01",
    "Peaky Blinders": "D:\\documents\\videos\\Movies\\Peaky Blinders",
}

video_mapping = {
    "cabinate of cureosities s1 e1": "Cabinet of Curiosities S01E01.mkv",
    "cabinate of cureosities s1 e2": "Cabinet of Curiosities S01E02.mkv",
    "cabinate of cureosities s1 e3": "Cabinet of Curiosities S01E03.mkv",
    "cabinate of cureosities s1 e4": "Cabinet of Curiosities S01E04.mkv",
    "cabinate of cureosities s1 e5": "Cabinet of Curiosities S01E05.mkv",
    "cabinate of cureosities s1 e6": "Cabinet of Curiosities S01E06.mkv",
    "cabinate of cureosities s1 e7": "Cabinet of Curiosities S01E07.mkv",
    "cabinate of cureosities s1 e8": "Cabinet of Curiosities S01E08.mkv",
    "old jumanji": "Jumanji 1995.mkv",
    "the revenant":"The Revenant.mkv",
    "the exorcist-believer":"The Exorcist-Believer.mkv",
    "dora and the lost city of gold":"Dora And The Lost City of Gold.mkv",
    "The Wheel of Time S01 E01": "The Wheel of Time S01 E01.mkv",
    "The Wheel of Time S01 E02": "The Wheel of Time S01 E02.mkv",
    "The Wheel of Time S01 E03": "The Wheel of Time S01 E03.mkv",
    "The Wheel of Time S01 E04": "The Wheel of Time S01 E04.mkv",
    "The Wheel of Time S01 E05": "The Wheel of Time S01 E05.mkv",
    "The Wheel of Time S01 E06": "The Wheel of Time S01 E06.mkv",
    "The Wheel of Time S01 E07": "The Wheel of Time S01 E07.mkv",
    "The Wheel of Time S01 E08": "The Wheel of Time S01 E08.mkv",
    "peaky blinders s1 e1":"Peaky Blinders S01E01.mkv",
    "peaky blinders s1 e2":"Peaky Blinders S01E02.mkv",
    "peaky blinders s1 e3":"Peaky Blinders S01E03.mkv",
    "peaky blinders s1 e4":"Peaky Blinders S01E04.mkv",
    "peaky blinders s1 e5":"Peaky Blinders S01E05.mkv",
    "peaky blinders s1 e6":"Peaky Blinders S01E06.mkv",
    "peaky blinders s2 e1":"Peaky Blinders S02E01.mkv",
    "peaky blinders s2 e2":"Peaky Blinders S02E02.mkv",
    "peaky blinders s2 e3":"Peaky Blinders S02E03.mkv",
    "peaky blinders s2 e4":"Peaky Blinders S02E04.mkv",
    "peaky blinders s2 e5":"Peaky Blinders S02E05.mkv",
    "peaky blinders s2 e6":"Peaky Blinders S02E06.mkv",
    "peaky blinders s3 e1":"Peaky Blinders S03E01.mkv",
    "peaky blinders s3 e2":"Peaky Blinders S03E02.mkv",
    "peaky blinders s3 e3":"Peaky Blinders S03E03.mkv",
    "peaky blinders s3 e4":"Peaky Blinders S03E04.mkv",
    "peaky blinders s3 e5":"Peaky Blinders S03E05.mkv",
    "peaky blinders s3 e6":"Peaky Blinders S03E06.mkv",
    "peaky blinders s4 e1":"Peaky Blinders S04E01.mkv",
    "peaky blinders s4 e2":"Peaky Blinders S04E02.mkv",
    "peaky blinders s4 e3":"Peaky Blinders S04E03.mkv",
    "peaky blinders s4 e4":"Peaky Blinders S04E04.mkv",
    "peaky blinders s4 e5":"Peaky Blinders S04E05.mkv",
    "peaky blinders s4 e6":"Peaky Blinders S04E06.mkv",
    "peaky blinders s5 e1":"Peaky Blinders S05E01.mkv",
    "peaky blinders s5 e2":"Peaky Blinders S05E02.mkv",
    "peaky blinders s5 e3":"Peaky Blinders S05E03.mkv",
    "peaky blinders s5 e4":"Peaky Blinders S05E04.mkv",
    "peaky blinders s5 e5":"Peaky Blinders S05E05.mkv",
    "peaky blinders s5 e6":"Peaky Blinders S05E06.mkv",
    "peaky blinders s5 e1":"Peaky Blinders S06E01.mkv",
    "peaky blinders s5 e2":"Peaky Blinders S06E02.mkv",
    "peaky blinders s5 e3":"Peaky Blinders S06E03.mkv",
    "peaky blinders s5 e4":"Peaky Blinders S06E04.mkv",
    "peaky blinders s5 e5":"Peaky Blinders S06E05.mkv",
    "peaky blinders s5 e6":"Peaky Blinders S06E06.mkv",
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Very Good Morning!")

    elif 12 <= hour < 18:
        speak("Very Good Afternoon!")

    elif 18 <= hour:
        speak("Very Good Evening!")

    else:
        speak("It's too late.\nGo to bed, Good Night!!")

    speak("I am Jarvo. Please tell me how may I help you today.")

def close_whatsapp():
    if platform.system() == 'Windows':
        process_name = 'WhatsApp.exe'
    elif platform.system() == 'Darwin':
        process_name = 'WhatsApp'
    elif platform.system() == 'Linux':
        process_name = 'whatsapp'

    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == process_time_ns: # type: ignore
            process.terminate()


def play_specific_video(query):
    try:
        video_file = None
        for directory_name, directory_path in video_directories.items():
            video_file = video_mapping.get(query.lower())
            if video_file:
                video_path = os.path.join(directory_path, video_file)
                if os.path.exists(video_path):
                    os.startfile(video_path)
                    speak(f"Playing video: {video_file}")
                    break

        if not video_file:
            speak("Sorry, I couldn't find the requested video.")
    except Exception as e:
        print(e)
        speak("An error occurred while playing the video.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
            return query
        except sr.UnknownValueError:
            speak("Could not listen audio")
        except sr.RequestError as e:
            speak(f"Could not request results; {e}")
        return None

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pssingh050205@gmail.com', 'virat@018')
    server.sendmail('pssingh050205@gmail.com', to, content)
    server.close()

def is_logical_question(query):
    if not query.endswith('?'):
        return False

    if not query.split(' ')[0].endswith(('who', 'what', 'when', 'where', 'why', 'how')):
        return False

    if len(query.split(' ')) < 3:
        return False

    return True

def process_query(query):
    if is_logical_question(query):
        speak(f"Searching Google for: {query}")
        results = subprocess.check_output(['google', 'search', query])
        speak(results)
    else:
        speak("Your question is not logically correct")


if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand()
        if query is not None:
            query = query.lower() # type: ignore

            if 'wikipedia' in query:
                try:
                    speak('Searching Wikipedia...')
                    query = query.replace('wikipedia', '')
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.DisambiguationError as e:
                    print(e)
                    speak("There are multiple results. Please specify your query.")
                except wikipedia.exceptions.PageError as e:
                    print(e)
                    speak("Sorry, I couldn't find any relevant information.")
                except Exception as e:
                    print(e)
                    speak("An error occurred while searching Wikipedia.")

            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com")

            elif 'play' in query:
                query_parts = query.split()
                video_query = " ".join(query_parts[1:])
                speak(f"Playing video: {video_query}")
                play_specific_video(video_query)

            elif 'open chrome' in query:
                chrome_path = "C:\\Users\\Dell\\OneDrive\\Desktop\\103 - Chrome.lnk"
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab("http://www.google.com")

            elif 'open incognito in chrome' in query:
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                subprocess.Popen([chrome_path, '--incognito'])

            elif 'open' in query and ('in C drive' in query or 'in D drive' in query):
                drive_letter = 'C' if 'in C drive' in query else 'D'
                folder_name = query.split('in')[0].strip().replace('open folder', '').strip()
                folder_path = f"{drive_letter}:\\{folder_name}"
                
                if os.path.exists(folder_path):
                    os.startfile(folder_path)
                    speak(f"Opening folder: {folder_name} in drive {drive_letter}")
                else:
                    speak(f"Folder '{folder_name}' in drive {drive_letter} not found.")

            elif 'open Control Panel' in query:
                try:
                    if platform.system() == 'Windows':
                        os.system('control')
                        speak("Opening Control Panel")
                    else:
                        speak("Sorry, Control Panel is only supported on Windows.")
                except Exception as e:
                    print(e)
                    speak("An error occurred while opening Control Panel.")

            elif 'open settings' in query:
                try:
                    if platform.system() == 'Windows':
                        os.system('start ms-settings:')
                        speak("Opening Settings")
                    else:
                        speak("Sorry, the Settings app is only supported on Windows.")
                except Exception as e:
                    print(e)
                    speak("An error occurred while opening Settings.")

            elif 'answer my question' in query:
                speak("Ask a logical question")
                question = takeCommand()
                process_query(question)

            elif 'open stackoverflow' in query:
                webbrowser.open("https://www.stackoverflow.com")

            elif 'open whatsapp' in query:
                os.startfile("C:\\Users\\Dell\\OneDrive\\Desktop\\WhatsApp.lnk")

            elif 'play music' in query:
                music_name, platform = query.split(' in ')[0], query.split(' in ')[1].strip()
                if platform == 'spotify':
                    try:
                        subprocess.call(['spotify', 'search', music_name])
                    except subprocess.CalledProcessError:
                        speak("Spotify is not installed. Please install Spotify to play music.")
                elif platform == 'youtube':
                    try:
                        subprocess.call(['youtube', 'search' + music_name])
                    except subprocess.CalledProcessError:
                        speak("YouTube is not installed. Please install YouTube to play music.")
                else:
                    speak("I do not recognize the platform you requested. Please specify Spotify or YouTube.")
            elif 'close browser' in query:
                os.system("taskkill /f /im chrome.exe")

            elif 'close youtube' in query:
                 os.system("taskkill /f /im chrome.exe")

            elif 'close whatsapp' in query:
                close_whatsapp()

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'email to partha' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "pssingh050205@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am unable to send the email at the moment.")

            elif 'thank you' in query:
                speak("You're welcome, sir. How can I assist you further?")

            elif 'may you audible' in query:
                speak("Yes sir! You can order me.")

            elif 'stop' in query:
                hour = datetime.datetime.now().hour
                if 23 <= hour and hour>=3:
                    speak("Good Night!!!")
                    break
                else:
                    speak("Bye bye!!\nTake care\nHave a nice day")
                    break

            else:
                print("Query not recognized")
                speak("I didn't understand your request. Please repeat.")