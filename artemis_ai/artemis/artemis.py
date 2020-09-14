# from googlesearch import search 
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
# import urllib2
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
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import lxml
import subprocess
import time
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


global songUrlSave
songUrlSave=''
remLists = []   
listNames = []
global commandSave
adrs = 'aoztanir25@gmail.com'
pswrd = 'LADOO256'
global quitStatus
quitStatus = 0
counter = 0

# //////////////////////////////////////////////////////////////////////////////////

# time.sleep(1.5)


# def stopFunc(command):
#     if 'stop' in command:
#         artemisResponse('Stopping Sir')



r = sr.Recognizer()
converter = pyttsx3.init() 
converter.setProperty('rate', 205) 
converter.setProperty('volume', 1) 


counter=0
#t -> s
def myCommand():
    # while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')
            #loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            command = myCommand();

        if 'stop' in command:
            browser= webdriver.Chrome("/Users/apple/Desktop/artemis_ai/artemis/chromeDri")
            browser.get(songUrlSave)
            browser.close()
            elem = browser.find_element_by_tag_name("body")
            elem.send_keys(Keys.CONTROL+"w") 
            artemisResponse('Stopping Sir')
            # quitStatus = 1
            return
        return command    
        
# stopThread = threading.Thread(target = stopFunc(myCommand()))
#s -> t
def artemisResponse(audio):
    print(audio)
    voice_id = "com.apple.speech.synthesis.voice.daniel"  
    # Use female voice 
    converter.setProperty('voice', voice_id) 
    converter.runAndWait() 
    converter.say(audio)
    converter.runAndWait() 
    # for line in audio.splitlines():
    #     os.system("say " + audio)

askCount = 0
comprehendCount=0

def assistant(command):
    # stopThread.start() 
    # while True:
    comprehendCount=0
    askCount = 0

    if 'artemis' in command or'arty' in command or'art' in command or'archie' in command or'artie' in command or 'open' in command or 'launch' in command or 'weather' in command or 'play' in command or 'playlist' in command or 'exit' in command or 'song' in command or 'farty' in command or  'party' in command:

        if 'open reddit' in command:
            if askCount == 1:
                return
            askCount = 1
            comprehendCount+=1
            redditSearch = re.search('open reddit (.*)', command)
            url = 'https://www.reddit.com/'
            if redditSearch:
                subreddit = redditSearch.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            artemisResponse('The Reddit content has been opened for you Sir.')
        
        if 'open my news' in command or 'open news' in command:
            if askCount == 1:
                return
            askCount = 1

            comprehendCount+=1
            newsSearch = re.search('open my news (.*)', command)
            url = 'https://news.google.com'
            # if redditSearch:
            #     subreddit = redditSearch.group(1)
            #     url = url + 'r/' + subreddit
            webbrowser.open(url)
            artemisResponse('Your news feed has been opened for you Sir.')
        
        elif 'tell me about' in command:
            if askCount == 1:
                return
            askCount = 1

            comprehendCount+=1
            reg_ex = re.search('tell me about (.*)', command)
            try:
                if reg_ex:
                    topic = reg_ex.group(1)
                    ny = wikipedia.page(topic)
                    artemisResponse(ny.content[:500].encode('utf-8'))
            except Exception as e:
                print(e)
                artemisResponse(e)

        if 'google news' in command:
            if askCount == 1:
                return
            askCount = 1

            comprehendCount+=1
            newsSearch = re.search('open my news (.*)', command)
            url = 'https://news.google.com'
            # if redditSearch:
            #     subreddit = redditSearch.group(1)
            #     url = url + 'r/' + subreddit
            webbrowser.open(url)
            artemisResponse('Your news feed has been opened for you Sir.')
        
        if 'email' in command:
            if askCount == 1:
                return
            askCount = 1

            comprehendCount+=1
            artemisResponse('Who is the email to Sir?')
            recipient = myCommand()
            if 'fun' in recipient:
                artemisResponse('What is the message Sir?')
                content = myCommand()
                # mail = smtplib.SMTP('aoztanir25.gmail.com', 587)
                # mail.ehlo()
                # mail.starttls()
                # mail.login('aoztanir25@gmail.com', 'LADOO256')
                # mail.sendmail('aoztanir25@gmail.com', 'aoztanir25@gmail.com', content)
                # mail.close()
                # artemisResponse('The email has been sent Sir.')
                s = smtplib.SMTP(host='smtp-mail.gmail.com', port=587)
                s.starttls()
                s.login(adrs, pswrd)
                s.send_message(content)
                s.quit()
            else:
                artemisResponse('I am not sure what you mean Sir')
        if 'launch' in command:
            if askCount == 1:
                return
            askCount = 1

            comprehendCount+=1
            reg_ex = re.search('launch (.*)', command)
            if reg_ex:
                appname = reg_ex.group(1)
                appname1 = appname+".app"
                subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
                artemisResponse('I have launched the desired application, Sir')
        
        if 'weather' in command:
            if askCount == 1:
                return
            askCount = 1

            reg_ex = re.search('weather in (.*)', command)
            comprehendCount+=1
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='fahrenheit')
                artemisResponse('Current weather in %s is %s. The maximum temperature is %0.2f degrees Fahrenheit and the minimum temperature is %0.2f degrees Fahrenheit Sir' % (city, k, x['temp_max'], x['temp_min']))
         
        if 'temperature' in command:
            if askCount == 1:
                return
            askCount = 1

            reg_ex = re.search('temperature in (.*)', command)
            comprehendCount+=1
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='fahrenheit')
                artemisResponse('Current weather in %s is %s. The maximum temperature is %0.2f degrees Fahrenheit and the minimum temperature is %0.2f degrees Fahrenheit Sir' % (city, k, x['temp_max'], x['temp_min']))
        
        if ' time ' in command:
            if askCount == 1:
                return
            askCount = 1

            import datetime
            now = datetime.datetime.now()
            artemisResponse('Current time is %d hours %d minutes Sir' % (now.hour, now.minute))
        if 'play song' in command or 'music' in command or 'jam' in command:
            if askCount == 1:
                return
            askCount = 1

            quitStatus=0
            comprehendCount+=1
            artemisResponse('Alright, I like where this is going, Sir.  What song shall I play? Would you like me to play your jam, sir?')
            mysong = myCommand()
            if 'yes' in mysong:
                mysong = "80s"
                if mysong:
                    flag = 0
                    url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                    page = requests.get(url)
                    soup1 = soup(page.content,"html.parser")
                    try:
                        soupa = soup1.findAll(attrs={'class':'yt-uix-tile-link'})[0]
                        if ('https://www.youtube.com' + soupa['href']).startswith("https://www.youtube.com/watch?v="):
                            flag = 1
                            flaga = flag
                            flaga+=1
                            final_url = 'https://www.youtube.com' + soupa['href']
                            # print(final_url)
                            webbrowser.open(final_url)
                            artemisResponse("The music has started, Sir! Happy Hacking!")
                            return
                            # if flaga == 2:
                            #     break
                    except IndexError:
                        artemisResponse('It seems like I am having trouble accessing this music, sir. Please try again later.')
            # if quitStatus == 1:
            #     return
            if mysong:
                flag = 0
                url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                page = requests.get(url)
                soup1 = soup(page.content,"html.parser")
                try:
                    soupa = soup1.findAll(attrs={'class':'yt-uix-tile-link'})[0]
                    if ('https://www.youtube.com' + soupa['href']).startswith("https://www.youtube.com/watch?v="):
                        flag = 1
                        flaga = flag
                        flaga+=1
                        final_url = 'https://www.youtube.com' + soupa['href']
                        print(final_url)
                        webbrowser.open(final_url)
                        artemisResponse('The song has been opened Sir')
                        # if flaga == 2:
                        #     break
                except IndexError:
                    artemisResponse('I have not found anything in Youtube Sir')
        
        if 'play the playlist' in command or 'play playlist' in command:
            if askCount == 1:
                return
            askCount = 1
            comprehendCount+=1
            if 'play the playlist' in command:
                reg_ex = re.search('play the playlist (.*)', command)
                mysong=reg_ex.group(1)
            if 'play playlist' in command:
                reg_ex = re.search('play playlist (.*)', command)
                mysong=reg_ex.group(1)
            flag = 0
            if mysong:
                url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+') + '+playlist'
                page = requests.get(url)
                soup1 = soup(page.content,"html.parser")
                try:
                    soupa = soup1.findAll(attrs={'class':'yt-uix-tile-link'})[0]
                    if ('https://www.youtube.com' + soupa['href']).startswith("https://www.youtube.com/watch?v="):
                        flag = 1
                        flaga = flag
                        flaga+=1
                        final_url = 'https://www.youtube.com' + soupa['href']
                        print(final_url)
                        webbrowser.open(final_url)
                        artemisResponse('The playlist has been opened Sir')
                        # if flaga == 2:
                        #     break
                except IndexError:
                    artemisResponse('I have not found anything in Youtube Sir')
                
                # if flag == 0:
                #     artemisResponse('I have not found anything in Youtube Sir')

        if 'play ' in command:
            # print("hi")
            if askCount == 1:
                return
            askCount = 1
            # quitStatus=0
            comprehendCount+=1
            songCount = 0
            if 'play the song' in command:
                if songCount != 1:
                    reg_ex = re.search('play the song (.*)', command)
                    mysong=reg_ex.group(1)
                    songCount+=1
            elif 'play song' in command:
                if songCount != 1:
                    reg_ex = re.search('play song (.*)', command)
                    mysong=reg_ex.group(1)
                    songCount+=1
            if 'play ' in command:
                if songCount != 1:
                    reg_ex = re.search('play (.*)', command)
                    mysong=reg_ex.group(1)
                    songCount+=1
                # if quitStatus == 1:
                #     return
                # print(mysong)
                if True:
                    flag = 0
                    url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                    print(url)
                    page = requests.get(url)
                    soup1 = soup(page.content,"html.parser")
                    try:
                        soupa = soup1.findAll(attrs={'class':'yt-uix-tile-link'})[0]
                        # print(soupa)
                        if ('https://www.youtube.com' + soupa['href']).startswith("https://www.youtube.com/watch?v="):
                            flag = 1
                            flaga = flag
                            flaga+=1
                            final_url = 'https://www.youtube.com' + soupa['href']
                            # print(final_url)
                            webbrowser.open(final_url)
                            songUrlSave=final_url
                            final_url = ''
                            if 'playlist' in command:
                                artemisResponse("The playlist has been opened, Sir")
                            else:
                                artemisResponse('The song has been opened, Sir')
                            # if flaga == 2:
                            #     break
                    except IndexError:
                        artemisResponse('I have not found anything in Youtube Sir')

        if 'play song' in command or 'music' in command or 'jam' in command:
            if askCount == 1:
                return
            askCount = 1

            quitStatus=0
            comprehendCount+=1
            artemisResponse('Alright, I like where this is going, Sir. What song shall I play? Would you like me to play your jam, sir?')
            mysong = myCommand()
            if 'yes' in mysong:
                mysong = "80s"
                if mysong:
                    flag = 0
                url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                page = requests.get(url)
                soup1 = soup(page.content,"html.parser")
                try:
                    soupa = soup1.findAll(attrs={'class':'yt-uix-tile-link'})[0]
                    if ('https://www.youtube.com' + soupa['href']).startswith("https://www.youtube.com/watch?v="):
                        flag = 1
                        flaga = flag
                        flaga+=1
                        final_url = 'https://www.youtube.com' + soupa['href']
                        print(final_url)
                        webbrowser.open(final_url)
                        artemisResponse("The music has started, Sir! Happy Hacking!")
                        return
                        # if flaga == 2:
                        #     break
                except IndexError:
                    pass
                    # artemisResponse('It seems like I am having trouble accessing this music, sir. Please try again later.')
            # if quitStatus == 1:
            #     return
            if mysong:
                flag = 0
                url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                page = requests.get(url)
                soup1 = soup(page.content,"html.parser")
                try:
                    soupa = soup1.findAll(attrs={'class':'yt-uix-tile-link'})[0]
                    if ('https://www.youtube.com' + soupa['href']).startswith("https://www.youtube.com/watch?v="):
                        flag = 1
                        flaga = flag
                        flaga+=1
                        final_url = 'https://www.youtube.com' + soupa['href']
                        print(final_url)
                        webbrowser.open(final_url)
                        artemisResponse('The song has been opened Sir')
                        # if flaga == 2:
                        #     break
                except IndexError:
                    artemisResponse('I have not found anything in Youtube Sir')

        if 'playlist ' in command:
            if askCount == 1:
                return
            askCount = 1

            comprehendCount+=1
            artemisResponse('Which playlist shall I play Sir?')
            mysong = myCommand()
            flag = 0
            if mysong:
                url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+') + '+playlist'
                page = requests.get(url)
                soup1 = soup(page.content,"html.parser")
                try:
                    soupa = soup1.findAll(attrs={'class':'yt-uix-tile-link'})[0]
                    if ('https://www.youtube.com' + soupa['href']).startswith("https://www.youtube.com/watch?v="):
                        flag = 1
                        flaga = flag
                        flaga+=1
                        final_url = 'https://www.youtube.com' + soupa['href']
                        print(final_url)
                        webbrowser.open(final_url)
                        artemisResponse('The playlist has been opened Sir')
                        # if flaga == 2:
                        #     break
                except IndexError:
                    artemisResponse('I have not found anything in Youtube Sir')
                
                # if flag == 0:
                #     artemisResponse('I have not found anything in Youtube Sir')

        if 'play me a video' in command or 'video' in command:
            if askCount == 1:
                return
            askCount = 1
            comprehendCount+=1
            artemisResponse('Which video shall I play Sir?')
            mysong = myCommand()
            flag = 0
            if mysong:
                url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                page = requests.get(url)
                soup1 = soup(page.content,"html.parser")
                try:
                    soupa = soup1.findAll(attrs={'class':'yt-uix-tile-link'})[0]
                except IndexError:
                    artemisResponse('I have not found anything in Youtube Sir')
                if ('https://www.youtube.com' + soupa['href']).startswith("https://www.youtube.com/watch?v="):
                        flag = 1
                        flaga = flag
                        flaga+=1
                        final_url = 'https://www.youtube.com' + soupa['href']
                        print(final_url)
                        webbrowser.open(final_url)
                        artemisResponse('The video has been opened Sir')
                        # if flaga == 2:
                        #     break
                if flag == 0:
                    artemisResponse('I have not found anything in Youtube Sir')


        
        if 'who are you' in command or 'what is your purpose' in command:
            if askCount == 1:
                return
            askCount = 1

            comprehendCount+=1
            artemisResponse('Hello Sir, My name is Artemis. You can call me arty, artemis or computer. I was created by Artemis Robotics as an experimental A.I.. My functionality and features improve every day, the more you utilize me, the better I get! Best of luck sir!')
        
        if 'website' in command:
            if askCount == 1:
                return
            askCount = 1

            comprehendCount+=1
            reg_ex = re.search('open website (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain
                webbrowser.open(url)
                artemisResponse('The website you have requested has been opened for you Sir.')
        
        if 'hello' in command:
            if askCount == 1:
                return
            askCount = 1

            comprehendCount+=1
            day_time = int(strftime('%H'))
            if day_time < 12:
                artemisResponse('Good morning Sir')
            elif 12 <= day_time < 18:
                artemisResponse('Good afternoon Sir')
            else:
                artemisResponse('Good evening Sir')    

        
        if 'headlines' in command:
            if askCount == 1:
                return
            askCount = 1
            comprehendCount+=1
            try:
                artemisResponse('How many headlines would you like Sir?')
                hNum=myCommand()
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                hNum=int(hNum)
                try:
                    hNum += 1
                except TypeError:
                    hNum=6
                for news in news_list[:int(hNum-1)]:
                    artemisResponse(news.title.text.encode('utf-8'))
            except Exception as e:
                    print(e)

        # if 'stop' in command:
        #     comprehendCount+=1
        #     artemisResponse('Stopping Sir')
        #     # t2.daemon = True
        #     print("jo")
        if 'make a list' in command:
            if askCount == 1:
                return
            askCount = 1
            comprehendCount+=1
            artemisResponse('What should I make a list of sir?')
            name = myCommand()
            artemisResponse('What are the items in the list sir?')
            listSave = myCommand()
            finalList = name+'\n '+listSave
            finalList = finalList.replace(" ", "\n")
            listSave = open("list.txt","a") 
            listSave.write("\n")
            listSave.write(finalList)
            listSave.close()
            artemisResponse('The list has been saved to the Artemis Directory')
        if 'timer for' in command:
            if askCount == 1:
                return
            askCount = 1
            comprehendCount+=1
            reg_ex = re.search('timer for (.*)', command)
            timerAmount = timerAmount = reg_ex.group(1)
            # if 'hours' in timerAmount or 'hour' in timerAmount:
            #     timerAmountHour = timerAmount
            #     timerAmountHour = timerAmountHour.replace(" hours", "")
            #     timerAmountHour = timerAmountHour.replace(" hour", "")
            #     hours = timerAmountHour[0]



            # timerAmount = timerAmount.replace(" minutes","")
            # timerAmount = timerAmount.replace(" min","")
            # timerAmount = int(timerAmount)
            # timerAmount = timerAmount+'+minute+timer+'+ 'start'
            timerAmount = timerAmount.replace(" ", "+")
            timerAmount = timerAmount + '+timer+start'
            url = "https://www.google.com/search?q="+ timerAmount + "&rlz=1C5CHFA_enUS804US805&oq=" + timerAmount + "&aqs=chrome..69i57.5440j0j1&sourceid=chrome&ie=UTF-8"
            webbrowser.open_new_tab(url)
            # , new = 2, autoraise = True
            artemisResponse("Got it, Sir. And thats starting now!")
            # print(timerAmount)
            # url = 
            # webbrowser.open(url)
        
        if 'alarm' in command and 'set' in command:
            pass



        if 'conversation' in command:
            if askCount == 1:
                return
            askCount = 1
            comprehendCount+=1
            artemisResponse('What would you like to converse about?')
            convMe = myCommand()
            if 'anything' in command or 'all' in command or 'any':
                artemisResponse("Would you like to learn more about me, Sir?")
                convMe = myCommand()
                if 'yes' in convMe or 'sure' in convMe or 'why not' in convMe:
                    artemisResponse("I can do quite a few things, Sir. A list of my features is located in the Artemis A.I. Directory")
                else:
                    artemisResponse('Alright Sir. No Problem. If you would like a list of my features just say hey artemis tell me your features.')
            else:
                artemisResponse("Sorry Sir, I cannot help with that yet")

        if 'features' in command:
            if askCount == 1:
                return
            askCount = 1
            artemisResponse("I can do quite a few things, Sir. A list of my features is located in the Artemis A.I. Directory")

        if 'quit' in command:
            if askCount == 1:
                return
            reg_ex = re.search('quit (.*)', command)
            killAppInput = timerAmount = reg_ex.group(1)
            askCount = 1
            comprehendCount+=1
            killAppInput = killAppInput.title()
            killApp = "killall -9 '%s'" %killAppInput
            artemisResponse('The app has been quit Sir')
            os.system(killApp)
            
        
        # if 'search google for' in command or 'search up' in command or 'search ' in command:
        #     if askCount == 1:
        #         return
        #     askCount = 1

        #     comprehendCount+=1
        #     reg_ex = re.search('search google for (.*)', command)
        #     try:
        #         if reg_ex:
        #             topic = reg_ex.group(1)
        #             for j in search(topic, tld="co.in", num=10, stop=10, pause=2): 
        #                 artemisResponse('Here is what I found Sir')
        #                 artemisResponse(j)
        #                 artemisResponse('Would you like me to open the webpage Sir?')
        #     except Exception as e:
        #         print(e)
        #         artemisResponse(e)

        if 'bluetooth' in command:
            pass
           


        if 'exit' in command or 'shut down' in command or 'shutdown' in command:
            if askCount == 1:
                return
            askCount = 1
            comprehendCount+=1
            artemisResponse('The experimental A.I. simulation has been shutdown for you sir')
            exit()
        
        
        if comprehendCount<1:
            randomNum = random.randint(1,5)
            if randomNum == 1:
                artemisResponse('Sorry, I did not understand what you said Sir')
            if randomNum == 2:
                artemisResponse('Could you repeat that Sir?')
            if randomNum == 3:
                artemisResponse('Sorry, I did not get that Sir')
            if randomNum == 4:
                artemisResponse('Could you say that again Sir?')
            if randomNum == 5:
                artemisResponse('Apologies Sir, I did not understand what you said')
                
                



# commandSave = ''
# t1 = threading.Thread(target=myCommand)
# t2= threading.Thread(target=assistant(myCommand()))

day_time = int(strftime('%H'))
if day_time < 12:
    artemisResponse('Good morning, Sir') 
elif 12 <= day_time < 18:
    artemisResponse('Good afternoon, Sir') 
else:
    artemisResponse('Good evening, Sir')
  


def mainFunc():
    while True:
        assistant(myCommand())
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=0.1)
        




mainFunc()

