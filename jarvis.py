import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'johnny' in command:
                johnny = command.replace('johnny', '')
                talk(command)

    except:
         pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt('Playing ..' + song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk("the time is" + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        google = wikipedia.summary(person, 1)
        print(google)
        talk(google)

    else:
        talk("please say the command again")

while True:
    run_alexa()