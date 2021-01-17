import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import weather_forecast as wf



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak():
    engine.say("Hi, I am Alexa. How can I help you?")
    engine.runAndWait()

speak()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is ' + time)
    elif 'google' in command:
        webbrowser.open('www.google.com')
    elif 'facebook' in command:
        webbrowser.open('www.facebook.com')
    elif 'gmail' in command:
        webbrowser.open('www.gmail.com')
    elif 'twitter' in command:
        webbrowser.open('www.twitter.com')
    elif 'weather' in command:
        wf.forecast(place="Tetovo", time="14:15:00", date="2021-01-17", forecast="daily")
    elif 'search for' or 'find me' or 'who is' in command:
        query = command.replace('search for', '')
        info = wikipedia.summary(query, 2)
        print(info)
        talk(info)
    else:
        talk("Please say the command again.")
while True:
    run_alexa()

