import speech_recognition as sr
import win32com.client
import os
import webbrowser
import openai
import datetime
import random
speaker = win32com.client.Dispatch("SAPI.SpVoice")
openai.api_key = "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"

def ai(prompt):
    text = f"Open AI response for Prompt: {prompt} \n ***************** \n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Write an application for artificial intelligence internship",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    #todo : wrap this inside a try catch
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/prompt- {random.randint(1, 31231324242)}", "w") as f:
        f.write(text)
def say(text):
    os.system(f" say {text}")

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
            if "using artificial intelligence".lower() in query.lower():
                ai(prompt=query)
