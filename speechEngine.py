import pyttsx3
import datetime
import speech_recognition as sr

def init_engine(RATE = 0,VOLUME = 0):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + RATE)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + VOLUME)
    return engine 

def speak(engine,text):
    engine.say(text)
    engine.runAndWait()

def wishMe(engine):
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning, Joshua.")
        print("Good Morning, Joshua.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, Joshua.")
        print("Good Afternoon, Joshua.")
    else:
        speak("Good Evening, Joshua.")
        print("Good Evening, Joshua.")

    engine.runAndWait()
    
def takeCommand(engine):
    r =  sr.Recognizer()
    with sr.Microphone() as source: #might throw an error
        print("Listening...")
        audio = r.listen(source)
        
    try:
        statement = r.recognize_google(audio, language = 'en-in')
        print("User said: " + statement)

    except Exception as e:
        speak(engine,"I didn't quite catch that.")
        return "None"

    return statement 

