import datetime
import pyttsx3
import speech_recognition as sr
import eel
import pywhatkit
import pyjokes
import wikipedia
import os
import time 





def speak(text):
    text = str(text)
    engine = pyttsx3.init()
    engine.setProperty('rate', 130) 
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()
@eel.expose
def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source :
        print('listening......')

        eel.DisplayMessage('listening......')
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10 , 6)

    try:
        print('recognizing..')
        eel.DisplayMessage('recognizing......')
        query = r.recognize_google(audio, language ='en-in')
        query = query.lower()
        if 'glass' in query:
                query = query.replace('glass', '')
                
        print(f"users said : {query}")
        eel.DisplayMessage(query)
        
        eel.ShowHood()
    except Exception as e:
        return ""
    
    return query.lower()

# text = takecommand()
# speak(text)

##welcome part of the glass where he intruduce him self 
@eel.expose
def welcome():
   text = "Hello I am Glass! How can i help you ?"
   speak(text)



@eel.expose
def allCommands( message = 1):
   
    if message==1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
        eel.ShowHood()

    
    try:
       # query = takecommand()
        print(query)
        if 'play' in query :
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            eel.ShowHood()
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
            eel.DisplayMessage(time)
            eel.ShowHood()
        elif 'date' in query:
            da = datetime.datetime.now().strftime("%d %m %y")
            speak('Current date is ' + da)
            eel.DisplayMessage(da)
            eel.ShowHood()
        elif 'are you single' in query:
            speak('I am in a relationship with wifi')
            eel.ShowHood()
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            eel.ShowHood()
        elif 'print' in query:
            query=query.replace('print','')
            speak("ok printing.....")
            eel.DisplayMessage(query)
            eel.ShowHood()
        elif 'speak' in query:
            query=query.replace('speak','')
            speak(query)
            eel.ShowHood()
        elif 'tamanna ' in query:
            speak("she is a fucking bitch")
            eel.ShowHood()
        elif 'atanu' in query:
            speak("he is a ass hole")
            eel.ShowHood()
        elif 'stop' in query:
            speak("ok")
            eel.ShowHood()
        elif 'who is ' in query:
            try:
                info = wikipedia.summary(query, 2)
                eel.DisplayMessage(info)
                speak(info)
            except:
                pywhatkit.search(query)
        elif "open" in query:
            try:
                from engine.features import openCommand
                openCommand(query)
            except:
                speak("Not found please update the database")
                #eel.ShowHood()
        else :
            from engine.features import chatBot
            chatBot(query)
        
    except:
        print("error") 
       
        eel.ShowHood()