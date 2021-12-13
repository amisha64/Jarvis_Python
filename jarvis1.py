import pyttsx3 #pip install pyttsx3 (For Speak)
import datetime 
import speech_recognition as sr #pip install SpeechRecognition, pip install pipwin, pipwin install pyaudio
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil # for cpu and battery pip install pustil Must have microsoft visual studio build tools 2014+ link:https://www.partitionwizard.com/partitionmanager/microsoft-visual-c-14-is-required.html
import pyjokes #pip install pyjokes
import pyautogui #pip install pyautogui (For Screenshot) also pip install pillow
import os
import time
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha #pip install wolframalpha
#To convert this .py file to .exe file, do pip install pyinstaller

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    Year=datetime.datetime.now().year
    Month=datetime.datetime.now().month
    Date= datetime.datetime.now().day
    speak("The current date is")
    speak(Date)
    speak(Month)
    speak(Year)

def wishme():
    speak("Hi Amisha")
    time_()
    date_()

    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    elif hour >=18 and hour <24:
        speak("Good Evening ")
    else:
        speak("Good Night")
    speak("Jarvis at your service. Please tell me how can I help you?")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        return None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #identifying ourselves on server
    server.starttls() #putting the connection into tls module
    # Enable low security in gmail 
    server.login('amishakirti6410@gmail.com', '9234412390')
    server.sendmail('amishakirti6410@gmail.com', to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Amisha Kirti/Pictures/Screenshots/screenshot.png")

if __name__ == '__main__':
    clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file
    clear()
    wishme()
    while True:
        query = TakeCommand().lower()
        # All the commands said by user will be 
		# stored here in 'query' and will be 
		# converted to lower case for easily 
		# recognition of command 

        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        
        elif 'wikipedia' in query: #command as query wikipedia
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's email: ")
                to = (reciept)
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")

        elif 'search chrome' in query:
            speak("What should I search ?")
            chromepath = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') #will only open sites ending with chrome
        
        elif 'open youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)

        elif 'search google' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'word' in query:
            speak("opening MS Word")
            word = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
            os.startfile(word)

        elif "write a note" in query:
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)
                
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 

        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")  
        
        elif 'play music' in query:
            
            songs_dir = "C:/Users/Amisha Kirti/Music"
            music = os.listdir(songs_dir)
            speak("Which song do you want to play? Select a number")
            ans = TakeCommand().lower()
            while('number' not in ans and ans!='random' and ans!='you choose' and ans!='any'):
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())
            if 'number' in ans:
                no = int(ans.replace('number',''))
            elif 'random' or 'any' or 'you choose' in ans:
                no = random.randint(1,50)
            
            os.startfile(os.path.join(songs_dir, music[no]))

        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remember that"+remember.read())

        elif 'news' in query:
            #newsapi.org used
            try:

                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=in&apiKey=9987d0ce18624e38b1f027139f4f318b')
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e)) 

         #show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        #calculation wolfram alpha registration required
        elif "calculate" in query:
            
            app_id = "K6E5A3-QWQR8TTT5L "
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        #General Questions
        elif "what is" in query or "who is" in query: 
			
			# Use the same wolframe API key 
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        #sleep-time or stop listening
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        #quit
        elif 'offline' in query:
            speak("going Offline")
            quit()
        