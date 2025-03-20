import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import tkinter as tk
from tkinter import Label, Button, Entry


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Welcome to Daksh-Technology. I am Jarvis. Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand. Can you please repeat?")
            return "None"
        except sr.RequestError:
            print("Could not request results, please check your internet connection.")
            return "None"
        
def close_tab():
    speak("Closing the current tab.")
    pyautogui.hotkey('ctrl', 'w')

def type_text(text):
    speak("Typing your text.")
    pyautogui.typewrite(text)

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except wikipedia.exceptions.PageError:
        speak("Sorry, no results found on Wikipedia.")

def open_website(site):
    webbrowser.open(site)

def search_google(query):
    speak("Searching Google...")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def search_youtube(query):
    speak("Searching YouTube...")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def play_music():
    music_dir = "C:\\Users\\Public\\Music"
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, songs[0]))
    else:
        speak("No music files found.")

def tell_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")

def open_application(app_name):
    apps = {
        "whatsapp": "C:\\Users\\User\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
        "instagram": "https://www.instagram.com",
        "email": "https://mail.google.com",
        "vs code": "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
        "notepad": "notepad.exe"
    }
    if app_name in apps:
        if "http" in apps[app_name]:
            webbrowser.open(apps[app_name])
        else:
            os.startfile(apps[app_name])
        speak(f"Opening {app_name}")
    else:
        speak("Application not found.")

def adjust_volume(action):
    if action == "increase":
        os.system("nircmd.exe changesysvolume 2000")
        speak("Volume increased")
    elif action == "decrease":
        os.system("nircmd.exe changesysvolume -2000")
        speak("Volume decreased")

def restart_system():
    speak("Restarting system")
    os.system("shutdown /r /t 1")

def shutdown_system():
    speak("Shutting down system")
    os.system("shutdown /s /t 1")

def handle_query():
    query = takeCommand()
    if 'close tab' in query or 'close this tab' in query:
        close_tab()
    elif 'text' in query:
        text_to_type = query.replace("text", "").strip()
        type_text(text_to_type)
    elif 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        search_wikipedia(query)
    elif "who is" in query or "what is" in query:
        search_wikipedia(query)
    elif 'open youtube' in query:
        open_website("https://www.youtube.com")
    elif 'open google' in query:
        open_website("https://www.google.com")
    elif 'search google for' in query:
        search_query = query.replace("search google for", "").strip()
        search_google(search_query)
    elif 'search youtube for' in query:
        search_query = query.replace("search youtube for", "").strip()
        search_youtube(search_query)
    elif 'play music' in query:
        play_music()
    elif 'the time' in query:
        tell_time()
    elif 'open' in query:
        app_name = query.replace("open", "").strip()
        open_application(app_name)
    elif 'increase volume' in query:
        adjust_volume("increase")
    elif 'decrease volume' in query:
        adjust_volume("decrease")
    elif 'restart system' in query:
        restart_system()
    elif 'shutdown' in query:
        shutdown_system()
    elif 'exit' in query:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("I am not sure how to help with that.")

def start_listening():
    speak("Jarvis is now active.")
    while True:
        handle_query()

def create_gui():
    root = tk.Tk()
    root.title("Daksh-Technology - Jarvis AI")
    root.geometry("500x500")
    root.config(bg="#121212")
    
    Label(root, text="Daksh-Technology", font=("Arial", 20, "bold"), bg="#121212", fg="#00FF00").pack(pady=10)
    Label(root, text="Jarvis AI Assistant", font=("Arial", 16), bg="#121212", fg="white").pack(pady=5)
    
    Button(root, text="Start Listening", command=start_listening, font=("Arial", 14), bg="#00FF00", fg="black", height=2, width=20).pack(pady=20)
    
    Label(root, text="Contact: 6377318844", font=("Arial", 12), bg="#121212", fg="white").pack(side="bottom", pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    wishMe()
    create_gui()
