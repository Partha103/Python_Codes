import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr
import uuid

api_key = "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"
lang = 'en'

openai.api_key = api_key

guy = ""

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)

                new_string = said.replace("jarvo", "")
                new_string = new_string.strip()
                print(new_string)
                completion = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=new_string,
                    temperature=0.7,
                    max_tokens=150,
                )
                text = completion.choices[0].text.strip()
                speech = gTTS(text=text, lang=lang, slow=False)
                file_name = f"welcome_{str(uuid.uuid4())}.mp3"
                speech.save(file_name)
                playsound.playsound(file_name, block=False)

            except Exception as e:
                print(f"Exception: {str(e)}")

        return said

    if "stop" in guy:
        break

    guy = get_audio()
