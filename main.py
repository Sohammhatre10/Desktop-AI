import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import datetime
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language= "en-in")
            print(f"User said: {query}")
            return query
        except Exception as es:
            return "Some error occured. Sorry some error occured"
if __name__ == '__main__':
    while True:
        speaker.Speak("Hello I'm Oreo AI")
        while True:
            print("Listening...")
            query = takeCommand()
            sites = [["youtube", "https://www.youtube.com/"], ["google", "https://www.google.com/"], ["codeforces" , "https://codeforces.com/"], ["codechef", "https://www.codechef.com"]]
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                     webbrowser.open(site[1])
                     speaker.Speak(f"Opening {[site[0]]} sir...")
            # speaker.Speak(query)
            if "time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                speaker.Speak(f"Sir the time is {strfTime}")
