import speech_recognition as sr
import pyttsx3 
import webbrowser 
from datetime import datetime

#create objects 
recogniser = sr.Recognizer() 
engine = pyttsx3.init() 

#listen funciton 
def listen():
    print('Listening.... ') 
    with sr.Microphone() as microphone:
        audio = recogniser.listen(microphone) 
    try:
        text = recogniser.recognize_google(audio) 
        print('You: ', text)
        return text.lower()
    except sr.UnknownValueError:
        print('Sorry, I cannot understand you...')
        return ''
    except sr.RequestError:
        print('Unable to connect speech recognition service')
        return '' 

#speak function 
def speak(text):
    print('Assistant: ', text)
    engine.say(text) 
    engine.runAndWait()

#Assistant starts
print('Welcome to Voice Assistant')
while True:
    command = listen() 
    if 'hello' in command:
        print('Hello, how can i help you') 
    elif 'time' in command:
        currenttime = datetime.now().strftime('%I:%M %p')
        speak(currenttime)
    elif 'open google' in command:
        speak('Opening Google')
        webbrowser.open('https://www.google.com')
    elif 'open youtube' in command:
        speak('Opening Youtube')
        webbrowser.open('https://www.youtube.com')
    elif command.startswith('search'):
        command = command.replace('search', '', 1).strip() 
        speak('Searching for' + command)
        url = 'https://www.google.com/search?q=' + command 
        webbrowser.open(url)