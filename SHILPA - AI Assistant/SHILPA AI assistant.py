import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import openai
import playsound 
from gtts import gTTS
import pyaudio
from youtubesearchpython import VideosSearch

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',200)

api_key = "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"
lang ='en'
openai.api_key = api_key

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print("Hello, Good Morning, I am SHILPA, your AI personal assistant")
        speak("Hello, Good Morning, I am SHILPA, your AI personal assistant")
        
        print("Tell me how can I help you now?")
        speak("Tell me how can I help you now?")
        
    elif hour >= 12 and hour < 18:
        print("Hello, Good Afternoon, I am SHILPA, your AI personal assistant")
        speak("Hello, Good Afternoon, I am SHILPA, your AI personal assistant")
        
        print("Tell me how can I help you now?")
        speak("Tell me how can I help you now?")
        
    else:
        print("Hello, Good Evening, I am SHILPA, your AI personal assistant")
        speak("Hello, Good Evening, I am SHILPA, your AI personal assistant")
        
        print("Tell me how can I help you now?")
        speak("Tell me how can I help you now?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


wishMe()

if __name__=='__main__':


    while True:
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            print('your personal assistant SHILPA is shutting down,Good bye')
            speak('your personal assistant SHILPA is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'SHILPA' in statement or 'give' in statement or 'write' in statement or 'I want' in statement:
            words = statement.split()
            new_string = ' '.join(words[1:])
            print(new_string) 
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":statement}])
            text = completion.choices[0].message.content
            speech = gTTS(text = text, lang=lang, slow=False, tld="com.au")
            speech.save("welcome1.mp3")
            playsound.playsound("welcome1.mp3")

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            print("Opening Youtube")
            speak("Opening Youtube")
            time.sleep(5)

        elif 'open flipkart' in statement:
            webbrowser.open_new_tab("https://www.flipkart.com")
            print("Opening Flipkart")
            speak("Opening Flipkart")
            time.sleep(5)

        elif 'open amazon' in statement:
            webbrowser.open_new_tab("https://www.amazon.com")
            print("Opening Amazon")
            speak("Opening Amazon")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            print("Opening Google chrome")
            speak("Opening Google chrome")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            print("Opening Google Mail")
            speak("Opening Google Mail")
            time.sleep(5)
            
        elif 'check my recent mail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            print("Opening Google Mail")
            speak("Opening Google Mail")
            time.sleep(5)
            
        elif 'open wikipedia' in statement:
            webbrowser.open_new_tab("https://en.wikipedia.org/")
            print("Opening wikipedia")
            speak("Opening wikipedia")
            time.sleep(5)    

        elif "weather" in statement:
            api_key = "d6e77886bff0e0976873ced3a70a19cf"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            print("Can you tell me your current city name?")
            speak("can you tell me your current city name?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature in kelvin unit = " +
                    str(current_temperature) +
                    "\n humidity (in percentage) = " +
                    str(current_humidiy) +
                    "\n description = " +
                    str(weather_description))
                speak(" Temperature in kelvin unit is " +
                    str(current_temperature) +
                    "\n humidity in percentage is " +
                    str(current_humidiy) +
                    "\n description  " +
                    str(weather_description))

            else:
                print("I couldn't find your city, please say that again")
                speak("I couldn't find your city, please say that again")


        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            print(
                'I am SHILPA, your personal virtual assistant. I am programmed to assist you by executing various tasks'
                ' and you can ask me anything!')
            speak(
                'I am SHILPA, your personal virtual assistant. I am programmed to assist you by executing various tasks'
                ' and you can ask me anything!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            print("I was built by a great team who consists of Maxmilan Selvan Fernando, Elapaka Srikumar and Sivaramakrishnan")
            speak("I was built by a great team who consists of Maxmilan Selvan Fernando, Elapaka Shreekumar and Sheevaramakrishnan")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            print("Here is stackoverflow")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            print('Here are some headlines from the Times of India,Happy reading')
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            speak("Searching now")
            webbrowser.open('https://www.google.com/search?q=' + statement)
            time.sleep(5)
            
        elif 'youtube' in statement or 'play' in statement:
            statement = statement.replace("search", "")
            speak("Searching now")
            webbrowser.open('https://www.youtube.com/results?search_query=' + statement)
            time.sleep(5)    

        elif 'calculate' in statement:
            print('I can answer to computational questions and what question do you want to ask now')
            speak('I can answer to computational questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "P6LRHQ-9X79L485J4"
            client = wolframalpha.Client('P6LRHQ-9X79L485J4')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)        

        elif "log off" in statement or "sign out" in statement:
            print("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "shutdown" in statement:
            os.system("shutdown /s /t 5")
            
        elif "exit" in statement or "stop" in statement:
            print("Thank you. Glad to assist you again!")
            speak("Thank you. Glad to assist you again!")
            break
        
        else:
            print("Sorry! For now, I don't have much data. My team is working on it. In future, I will be able to answer that. Thank you")
            speak("Sorry! For now, I don't have much data, My team is working on it, In future, I will be able to answer that, Thank you")
            
time.sleep(3)
