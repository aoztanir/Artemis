import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
# import vlc
import urllib
import urllib2
import json
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen
import wikipedia
import random
from time import strftime
doNothing=0
import pyttsx3 
import random
from setuptools import setup
import os
import imageio
from PIL import ImageTk, Image
from pathlib import Path
from PIL import ImageTk, Image
import threading
from multiprocessing import Process
import tkinter


    
global commandSave

# //////////////////////////////////////////////////////////////////////////////////


print("please say something")
r = sr.Recognizer()
converter = pyttsx3.init() 
converter.setProperty('rate', 210) 
converter.setProperty('volume', 1) 

#t -> s
def myCommand():
    # while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')
            #loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            command = myCommand();

        if 'stop' in command:
            aoztanirResponse('Stopping Sir')
        
        return command    
        

#s -> t
def aoztanirResponse(audio):
    print(audio)
    voice_id = "com.apple.speech.synthesis.voice.daniel"  
    # Use female voice 
    converter.setProperty('voice', voice_id) 
    converter.runAndWait() 
    converter.say(audio)
    converter.runAndWait() 
    # for line in audio.splitlines():
    #     os.system("say " + audio)

comprehendCount=0

def assistant(command):
    # while True:
        comprehendCount=0

        if 'artemis' in command or'arty' in command or'art' in command or'archie' in command or'artie' in command or 'open' in command or 'launch' in command or 'weather' in command or 'play' in command or 'playlist' in command or 'exit' in command or 'song' in command:

            if 'open reddit' in command:
                comprehendCount+=1
                redditSearch = re.search('open reddit (.*)', command)
                url = 'https://www.reddit.com/'
                if redditSearch:
                    subreddit = redditSearch.group(1)
                    url = url + 'r/' + subreddit
                webbrowser.open(url)
                aoztanirResponse('The Reddit content has been opened for you Sir.')
            
            if 'open my news' in command or 'open news' in command:
                comprehendCount+=1
                newsSearch = re.search('open my news (.*)', command)
                url = 'https://news.google.com'
                # if redditSearch:
                #     subreddit = redditSearch.group(1)
                #     url = url + 'r/' + subreddit
                webbrowser.open(url)
                aoztanirResponse('Your news feed has been opened for you Sir.')
            
            elif 'tell me about' in command:
                comprehendCount+=1
                reg_ex = re.search('tell me about (.*)', command)
                try:
                    if reg_ex:
                        topic = reg_ex.group(1)
                        ny = wikipedia.page(topic)
                        aoztanirResponse(ny.content[:500].encode('utf-8'))
                except Exception as e:
                    print(e)
                    aoztanirResponse(e)

            if 'google' in command:
                comprehendCount+=1
                newsSearch = re.search('open my news (.*)', command)
                url = 'https://news.google.com'
                # if redditSearch:
                #     subreddit = redditSearch.group(1)
                #     url = url + 'r/' + subreddit
                webbrowser.open(url)
                aoztanirResponse('Your news feed has been opened for you Sir.')
            
            if 'email' in command:
                comprehendCount+=1
                aoztanirResponse('Who is the email to Sir?')
                recipient = myCommand()
                if 'fun' in recipient:
                    aoztanirResponse('What is the message Sir?')
                    content = myCommand()
                    mail = smtplib.SMTP('aoztanir25.gmail.com', 587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login('aoztanir25@gmail.com', 'LADOO256')
                    mail.sendmail('aoztanir25@gmail.com', 'aoztanir25@gmail.com', content)
                    mail.close()
                    aoztanirResponse('The email has been sent Sir.')
                else:
                    aoztanirResponse('I am not sure what you mean Sir')
            if 'launch' in command:
                comprehendCount+=1
                reg_ex = re.search('launch (.*)', command)
                if reg_ex:
                    appname = reg_ex.group(1)
                    appname1 = appname+".app"
                    subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
                    aoztanirResponse('I have launched the desired application, Sir')
            
            if 'weather' in command:
                reg_ex = re.search('weather in (.*)', command)
                comprehendCount+=1
                if reg_ex:
                    city = reg_ex.group(1)
                    owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                    obs = owm.weather_at_place(city)
                    w = obs.get_weather()
                    k = w.get_status()
                    x = w.get_temperature(unit='celsius')
                    aoztanirResponse('Current weather in %s is %s. The maximum temperature is %0.2f degree celcius and the minimum temperature is %0.2f degree celcius Sir' % (city, k, x['temp_max'], x['temp_min']))
            
            if 'time' in command:
                import datetime
                now = datetime.datetime.now()
                aoztanirResponse('Current time is %d hours %d minutes Sir' % (now.hour, now.minute))

            if 'song' in command:
                comprehendCount+=1
                aoztanirResponse('What song shall I play Sir?')
                mysong = myCommand()
                if mysong:
                    flag = 0
                    url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup1 = soup(html,"lxml")
                    for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
                        if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                            flag = 1
                            flaga = flag
                            flaga+=1
                            final_url = 'https://www.youtube.com' + vid['href']
                            webbrowser.open(final_url)
                            aoztanirResponse('The song has been opened Sir')
                            if flaga == 2:
                                break
                        if flag == 0:
                            aoztanirResponse('I have not found anything in Youtube Sir')

            if 'playlist' in command:
                comprehendCount+=1
                aoztanirResponse('Which playlist shall I play Sir?')
                mysong = myCommand()
                mysong=mysong+" playlist"
                if mysong:
                    flag = 0
                    url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup1 = soup(html,"lxml")
                    for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
                        if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                            flag = 1
                            flaga = flag
                            flaga+=1
                            final_url = 'https://www.youtube.com' + vid['href']
                            webbrowser.open(final_url)
                            aoztanirResponse('The playlist has been opened Sir')
                            if flaga == 2:
                                break
                        if flag == 0:
                            aoztanirResponse('I have not found anything in Youtube Sir')
            if 'who are you' in command or 'you' in command:
                comprehendCount+=1
                aoztanirResponse('Hello Sir, My name is Artemis. You can call me arty, artemis or computer. I was created by Artemis Robotics as an experimental A.I.. My functionality and features improve every day, the more you utilize me, the better I get! Best of luck sir!')
            
            if 'open website' in command:
                comprehendCount+=1
                reg_ex = re.search('open website (.+)', command)
                if reg_ex:
                    domain = reg_ex.group(1)
                    print(domain)
                    url = 'https://www.' + domain
                    webbrowser.open(url)
                    aoztanirResponse('The website you have requested has been opened for you Sir.')
            if 'hello' in command:
                comprehendCount+=1
                day_time = int(strftime('%H'))
                if day_time < 12:
                    aoztanirResponse('Hello Sir. Good morning')
                elif 12 <= day_time < 18:
                    aoztanirResponse('Hello Sir. Good afternoon')
                else:
                    aoztanirResponse('Hello Sir. Good evening')    


            if 'exit' in command or 'shut down' in command or 'shutdown' in command:
                comprehendCount+=1
                aoztanirResponse('The experimental A.I. simulation has been shutdown for you sir')
                exit()
            
            if 'headlines' in command:
                try:
                    news_url="https://news.google.com/news/rss"
                    Client=urlopen(news_url)
                    xml_page=Client.read()
                    Client.close()
                    soup_page=soup(xml_page,"xml")
                    news_list=soup_page.findAll("item")
                    for news in news_list[:15]:
                        aoztanirResponse(news.title.text.encode('utf-8'))
                except Exception as e:
                        print(e)

            # if 'stop' in command:
            #     comprehendCount+=1
            #     aoztanirResponse('Stopping Sir')
            #     # t2.daemon = True
            #     print("jo")
            
            if comprehendCount<1:
                randomNum = random.randint(1,5)
                if randomNum == 1:
                    aoztanirResponse('Sorry, I did not understand what you said Sir')
                if randomNum == 2:
                    aoztanirResponse('Could you repeat that Sir?')
                if randomNum == 3:
                    aoztanirResponse('Sorry, I did not get that Sir')
                if randomNum == 4:
                    aoztanirResponse('Could you say that again Sir?')
                if randomNum == 5:
                    aoztanirResponse('Apologies Sir, I did not understand what you said')



# def stopFunc(command):
#     if 'stop' in command:
#         aoztanirResponse('Stopping Sir')


# commandSave = ''
# t1 = threading.Thread(target=myCommand)
# t2= threading.Thread(target=assistant(myCommand()))

def mainFunc():
    while True:
        assistant(myCommand())
    print("hi")

TK_SILENCE_DEPRECATION=1


window = tkinter.Tk()


B = tkinter.Button(window, text ="Hello", command=threading.Thread(target=mainFunc).start())

B.pack()
window.geometry('1500x857')
window.mainloop()



# window = tkinter.Tk()

# window.title("ARTY AI")

# # lbl = tkinter.Label(window, text="ARTY AI", font=("Arial Bold", 50))
# # lbl.pack

# button = tkinter.Button(window, text = 'INITIATE', command=threading.Thread(target=mainFunc).start())
# button.pack

# # lbl.grid(column=0, row=0)
# # window.geometry('1500x857')
# TK_SILENCE_DEPRECATION=1
# window.mainloop()