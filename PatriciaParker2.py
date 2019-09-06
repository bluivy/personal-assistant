import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
def say(audiostring):
    print(audiostring)
    tts=gTTS(text=audiostring,lang='en-uk')
    tts.save("pcvoice.mp3")
    os.system("start pcvoice.mp3")
def recordaudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        audio=r.listen(source)
    data=""
    try:
        data=r.recognize_google(audio)
        print("you said"+data)
    except sr.UnknownValueError:
        print("I didnt quite get what you said")
    except sr.RequestError as e:
        print("There are some glitches I guess;{0}".format(e))
    return data
def Nova(data):
    if "how are you" in data:
        say("I am fine Nivya,Thanks for the concern")
    elif "what time is it" in data:
        say(ctime())
    elif "what is your name" in data:
        say("I am first generation personal assistant,My name is PatriciaParker")
    elif "what can you do" in data:
        say("As of now I can tell time for you")
        say("do you wanna know what time is it?")
        say(ctime())
    elif "tell a joke in data" in data:
        say("I am sorry im not programmed to do that")
    
time.sleep(2)
say("This is PatriciaParker,I am glad to be of help")
while 1:
    data=recordaudio()
    Nova(data)
        
        

        
   
    
        
    
    
    
