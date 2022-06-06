import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!Suraj")   

    else:
        speak("Good Evening!suraj")  

    speak("I am your jarvis. how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print(" Can you say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('surajxuraj@gmail.com', 'your-password-here')
    server.sendmail('surajxuraj@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube wait for a second")
            webbrowser.open("youtube.com")

        elif 'play my favourite song' in query:
            speak("playing your favourite song wait for a second")
            music_dir="C:\\Users\\suraj\\Music\\Playlists\\Lil_Wayne_-_What_About_Me_(Lyrics)_Feat._Post_Malone.m4a"
            #  songs = os.listdir(music_dir)
            os.startfile(music_dir)

        elif 'open google' in query:
            speak("opening google wait for a second")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'open brave' in query:
            speak("opening brave wait for a second")
            brave_dir= "C:\\Users\\suraj\\OneDrive\\Desktop\\brave - Shortcut.lnk"
            os.startfile(brave_dir)

        elif 'open instagram' in query:
            speak("opening instagram wait for a second")
            instagram_dir="C:\\Users\\suraj\\OneDrive\\Desktop\\Instagram.lnk" 
            os.startfile(instagram_dir)

        elif 'open eclipse' in query:
            speak("opening eclipse wait for a second")
            eclipse_dir="C:\\Users\\suraj\\OneDrive\\Desktop\\Eclipse IDE for Java Developers - 2021-06.lnk"
            os.startfile(eclipse_dir)

        elif 'open whatsapp' in query:
            speak("opening whatsapp wait for a second")
            whatsapp_dir="C:\\Users\\suraj\\OneDrive\\Desktop\\WhatsApp.lnk"
            os.startfile(whatsapp_dir)

        elif 'open Facebook' in query:
            speak("opening facebook wait for a second")
            Facebook_dir="C:\\Users\\suraj\\OneDrive\\Desktop\\Facebook.lnk"
            os.startfile(Facebook_dir)


        elif 'play music' in query:
            speak("playing music wait for a second")
            music_dir = "C:\\Users\\suraj\\OneDrive\\Desktop\\audios"
            songs = os.listdir(music_dir)
            # print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f", the time is {strTime}")

        elif 'open code' in query:
            speak("wait for a second opening code")
            codePath = "C:\\Users\\suraj\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)
            # os.close(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "surajxuraj@gmai.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry to say you that i am not able to send this email") 
                
        elif'what is my name' in query:
            speak("your name is Suraj mandal")  

        elif'who are you' in query:
            speak("I am your jarvis sir!")

        elif 'quit' in query or 'exit' in query or 'close' in query:
             speak("Thanks you for using Jarvis")
             exit() 

