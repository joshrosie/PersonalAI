#import speech_recognition as sr
# import pyttsx3
# import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import ecapture
import wolframalpha
import json
import requests
import speechEngine as se

if __name__=='__main__':
    x = se.init_engine()
    se.wishMe(x)
    while True:
        se.speak(x,"How can I help you?")
        statement = se.takeCommand(x).lower()
        print(statement)
        if statement == 0:
            continue
    
        if "goodbye" in statement:
            se.speak(x,"Goodbye Joshua.")
            break