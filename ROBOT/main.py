import pyttsx3
import os
import speech_recognition as sr
import time
from model import load_model
model = load_model()

system_template = 'A chat between a curious user and an artificial intelligence assistant.'
prompt_template = 'USER: {0}\nASSISTANT: '
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def log(log: str):
    """
    Print and write to status.txt
    """
    print(log)
    with open("status.txt", "w") as f:
        f.write(log)


sr.Microphone()
r = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Hello")
text = listen()

while True:
    if text != "None":
        with model.chat_session(system_template, prompt_template):
            response = model.generate(prompt=text, temp=0.7, max_tokens=100)
            speak(response)
            try :
                text = listen()
            except ValueError as e:
                speak("I did not understand what you said")
                text = listen()
                if text == "None":
                    break
                else :
                    continue

            print("Thinking...")
            print(response)
            time.sleep(2)
            continue

    elif text == "goodbye" or text == "bye" or text == "shut down" or text == "exit" or text == "quit" or text == "stop" or text == "close" or text == "end" or text == "finish" or text == "terminate" or text == "kill":
        speak("Goodbye")
        break

    else:
        speak("I did not understand what you said")
        text=listen()
        time.sleep(2)
        continue