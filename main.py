import speech_recognition as sr
import webbrowser
import pyttsx3 #text to speech
import musicLibrary
import requests
import google.generativeai as genai

recognizer = sr.Recognizer()
newsapi = "56628ff9367a44a580a771df30677b2f"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def aiProcess(command):
    genai.configure(api_key="Your_Api_Key")

    model = genai.GenerativeModel("gemini-2.0-flash")

    chat = model.start_chat()

    response = chat.send_message(command)
    return response.text

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    
    elif "open linkdin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] #splits the name into play perfect and when it takes 1 it takes play so it recognizes the play word
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?q=trump&apiKey={newsapi}")
        if r.status_code == 200:
            #Parse the JSON response
            data = r.json()

            #Extract the article
            articles = data.get('articles', [])

            #Print the headlnes
            for article in articles:
                speak(article['title'])

    else:
        #Let openAI handle the req
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #listen for word jarvis
        #obtain audio from microphone
        r = sr.Recognizer()
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
