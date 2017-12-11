#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import argparse
import base64
import httplib2
import os
from google.cloud import translate
import speech_recognition as sr

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/lupe/Documents/Vision2-befbab1fbecb.json"

translate_client = translate.Client()
r = sr.Recognizer()
target = 'es'

os.system('espeak -v en -a 200 "I would translate your message"')  


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=5)
    print("Say something")
    os.system('feh -F /home/lupe/Desktop/Traduccion/maxresdefault.jpg &')	
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    os.system('espeak -v en -a 200 "You said {}"'.format(r.recognize_google(audio))) 
    translation = translate_client.translate(format(r.recognize_google(audio)),target_language=target)
  
    os.system('espeak -v es-la -a 200 "Tu dijiste {}"'.format(translation['translatedText']))
    os.system*("killall -9 feh")

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


