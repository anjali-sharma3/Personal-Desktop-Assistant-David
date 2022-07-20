from ast import operator
from audioop import add, mul
from cgitb import text
from http import server
from re import sub
import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib  # this module is used to send email
# getting the reference to an engine instance(using the Microsoft's Sapi5 driver)
engine = pyttsx3.init('sapi5')
# getting the value of engine's (sapi5's) voice property
voices = engine.getProperty('voices')
# getting the value of engine's (sapi5's) volume property
volume = engine.getProperty('volume')

engine.setProperty('volume', volume-2)  # volume setting
# using the system voice named as "David"
engine.setProperty('voice', voices[0].id)


def speak(text):  # This method will speak text into voice
    engine.say(text)
    engine.runAndWait()


def wish():  # This method will make David to wish me Good Morning/afternoon/evening and will give introduction
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning Anjali")
    elif hour > 12 and hour <= 17:
        speak("Good afternoon Anjali")
    else:
        speak("Good evening Anjali")
    speak("I am Devid ,your personal desktop assistant and I am here to help you")


def davidCommand():  # This method will take command for David(Desktop Assistant) using system's Microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:   # use the default microphone as the audio source
        print('Listening......')
        text = r.listen(source)
        # r.pause_threshold = 1
    try:
        print("Recognizing.....")
        query = r.recognize_google(text, language="en-in")
        print("You said:- \n", query)

    except Exception as e:
        print("Please speak again....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # used to identify on SMTP server
    # Put the SMTP connection in TLS (Transport Layer Security) mode.
    server.starttls()
    # Log in on an SMTP server that requires authentication. The arguments are the username and the password to authenticate with
    server.login('alexa@gmail.com', 'password')
    server.sendmail('alexa@gmail.com', to, content)
    server.close()                



if __name__ == "__main__":
    wish()
    # here is the logic for performing actions by David
    if 1:
        query = davidCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia..")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=10)
            speak(wikipedia)
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("Opening Youtube")
        elif 'party songs' in query or 'play songs ' in query or 'play party music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=0CmcaWyzPtM")
            speak("Playing .....")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            speak('opening google..')
        elif 'tell me time' in query or 'time' in query or 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'date' in query or 'what is date today' in query:
            today=date.today()
            d1=today.strftime("%d/%m/%Y")
            speak(f"today is {d1}")   
        elif 'who are you' in query or "Tell me about Yourself" in query:
            speak("I am david. I am created by Anjali Sharma. I am her personal desktop assistant. I want to make your work easy")
        elif 'open vs code' in query or 'open code' in query:
            vsPath = "C:\\Users\\anjali sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsPath)
            speak('opening vs code..')
        elif 'open zoom' in query:
            zoomPath = "C:\\Users\\anjali sharma\\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)
            speak('opening zoom')   
        elif 'exit' in query or 'quit' in query or 'ruk jao' in query:
            speak('Ok')
            exit()    
        elif 'send email':
             speak("To whom do you want to send email?")
             emailNames = {  # creating a dictionay of some names to send email
                "anjali": "anjalimbd.10201@gmail.com",
                "krishna": "krishnasharma98@gmail.com",
                "John": "John123@gmail.com"
             }
             try:
                speak("Tell the content of email")
                # whatever command will be given to david will store in content variable
                content = davidCommand()
                if list(emailNames[0]):
                    to = "anjalimbd.10201@gmail.com"
                elif list(emailNames[1]):
                    to = "krishnasharma98@gmail.com"
                elif list(emailNames[2]):
                    to = "John123@gmail.com"
                sendEmail(to, content)
                speak("email sent")
             except Exception as e:
                speak("Sorry I am unable to send email at this time")
        
