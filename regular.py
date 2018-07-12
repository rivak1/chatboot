import speech_recognition as sr
from gtts import gTTS
import threading
import pyglet
import time
import tkinter as tk
import threading
global f,question
lock=threading.Lock()
f=0
speech=sr.Recognizer()
def Welcomepage():
    a=input("enter your name-:")
    print("Wait siri is replying")
    db = open('rivak.txt', 'a')
    obj = gTTS(text="Hello %s Welcome to MY chatboot"%(a), lang='en')
    file = 'save.mp3'
    obj.save(file)
    res = pyglet.media.load(file, streaming=False)
    res.play()
    time.sleep(res.duration)
    db = open('rivak.txt', 'a')
    obj1 = gTTS(text="%s Enter your question" % (a), lang='en')
    file = 'save.mp3'
    obj1.save(file)
    res1 = pyglet.media.load(file, streaming=False)
    res1.play()
    time.sleep(res1.duration)
def Questionpage():
 while 1:
    global question
    print('question-:')
    global f
    db=open('rivak.txt','r')
    data=db.readlines()
    db.close()
    speech=sr.Recognizer()
    with sr.Microphone() as Mic:
        audio=speech.listen(Mic)
    try:
        lock.acquire()
        question = speech.recognize_google(audio)
        print(question)
        for i in data:
            i=i.split(':')
            if i[0]==question:
                print(i[0])
                value=i[1]
                print(value)
                f=1
                obj=gTTS(text=value,lang='en')
                file='save.mp3'
                obj.save(file)
                res=pyglet.media.load(file,streaming=False)
                res.play()
                time.sleep(res.duration)
            if question=='break':
                exit()
        else:
            lock.release()
            print('i')
            if f == 0:
                db = open('rivak.txt', 'a')
                print("What you say in your Language Please Give me answer i store in  my storage")
                obj = gTTS(text="What you say in your Language Please Give me answer i store in  my storage", lang='en')
                file = 'save.mp3'
                obj.save(file)
                res = pyglet.media.load(file, streaming=False)
                res.play()
                time.sleep(res.duration)
                with sr.Microphone() as Mic:
                    audio = speech.listen(Mic)
                try:
                    Answer = speech.recognize_google(audio)
                    db.write('\n' + question + ':' + Answer)
                    db.close()
                except Exception:
                    db = open('rivak.txt', 'a')
                    obj = gTTS(text="Ok BY BY", lang='en')
                    file = 'save.mp3'
                    obj.save(file)
                    res = pyglet.media.load(file, streaming=False)
                    res.play()
                    time.sleep(res.duration)
                    exit()
    except Exception:
        print("sorry i not recognsie it")
        break
def Notind():


        global f
        if f==0:
            db=open('rivak.txt','a')
            print("What you say in your Language Please Give me answer i store in  my storage")
            obj = gTTS(text="What you say in your Language Please Give me answer i store in  my storage", lang='en')
            file = 'save.mp3'
            obj.save(file)
            res = pyglet.media.load(file, streaming=False)
            res.play()
            time.sleep(res.duration)
            with sr.Microphone() as Mic:
                audio = speech.listen(Mic)
            try:
                    Answer = speech.recognize_google(audio)
                    db.write('\n'+question+':'+Answer)
                    db.close()
            except Exception:
                db = open('rivak.txt', 'a')
                obj = gTTS(text="Ok BY BY", lang='en')
                file = 'save.mp3'
                obj.save(file)
                res = pyglet.media.load(file, streaming=False)
                res.play()
                time.sleep(res.duration)
                exit()
thread=[]
thread.append(threading.Thread(target=Welcomepage))
thread.append(threading.Thread(target=Questionpage))
thread.append(threading.Thread(target=Notind))
for i in thread:
        i.start()
        i.join()

