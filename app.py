from flask import Flask, render_template, request
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import threading

app = Flask(__name__)

# Function to perform speech recognition
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening..')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print('recognizing...')
            data = recognizer.recognize_google(audio)
            print(data)
            return data.lower()
        except sr.UnknownValueError:
            print("Not Understand")

# Function to perform text-to-speech
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)
    engine.say(x)
    engine.runAndWait()

# Flag to control Jarvis activation
activate_jarvis = False

# Function to activate Jarvis
def activate_jarvis_func():
    global activate_jarvis
    speechtx('Jarvis activated')
    while activate_jarvis:
        data1 = sptext()
        if 'your name' in data1:
            name = 'my name is jarvis'
            speechtx(name)
        elif 'old are you' in data1:
            age = 'i am 20 years old'
            speechtx(age)
        elif 'time' in data1:
            time = datetime.datetime.now().strftime('%I%M%p')
            speechtx(time)
        elif 'youtube' in data1:
            webbrowser.open('https://www.youtube.com/')
            speechtx('Opening youtube..keep hold!')
        elif 'insta' in data1:
            webbrowser.open('https://www.instagram.com/?hl=en')
            speechtx('opening Instagram login Page')
        elif 'facebook' in data1:
            webbrowser.open('https://www.facebook.com/')
            speechtx('Opening facebook')
        elif 'git' in data1:
            webbrowser.open('https://github.com/account/enterprises/new')
            speechtx('opening github.com my programmer vishal!')
        elif 'deva deva' in data1:
            webbrowser.open('https://www.youtube.com/watch?v=mNuhKUOD_A0')
            speechtx('playing Your favourite song deva deva ')
        elif 'chat' in data1:
             webbrowser.open('https://chat.openai.com/c/95b78d14-6582-445f-9cb9-b9913834e799')
             speechtx('opening chatgpt from openai')
        elif 'whatsapp' in data1:
             webbrowser.open('https://web.whatsapp.com/')
             speechtx('opening whatsapp...keep chatting with people')
        elif 'joke' in data1:
            joke_1 = pyjokes.get_joke(language='en', category='neutral')
            print(joke_1)
            speechtx(joke_1)
        elif 'exit' in data1:
            speechtx('Goodbye')
            activate_jarvis = False
        elif 'vishal' in data1:
            speechtx('vishaal is my developer , my darling, my honey , my baby , my everything, i love my vishaal')

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for activating Jarvis
@app.route('/activate_jarvis', methods=['POST'])
def activate_jarvis_route():
    global activate_jarvis
    activate_jarvis = True
    threading.Thread(target=activate_jarvis_func).start()
    return 'Jarvis is activated'

# Route for stopping Jarvis
@app.route('/stop_jarvis', methods=['POST'])
def stop_jarvis():
    global activate_jarvis
    activate_jarvis = False
    return 'Jarvis is stopped'

if __name__ == '__main__':
    app.run(debug=True)