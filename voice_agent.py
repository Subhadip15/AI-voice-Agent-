import os
import speech_recognition as sr
import pyttsx3
import time

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("🗣 You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that")
        return ""
    except sr.RequestError:
        speak("Internet issue")
        return ""

def execute_command(command):
    if "shut down" in command or "shutdown" in command:
        speak("Shutting down your laptop")
        time.sleep(1)
        os.system("shutdown /s /t 0")

    elif "restart" in command:
        speak("Restarting your laptop")
        time.sleep(1)
        os.system("shutdown /r /t 0")

    elif "sleep" in command:
        speak("Putting system to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "exit" in command or "stop" in command:
        speak("Stop AI")
        exit()

    else:
        speak("Command not recognized")

def main():
    speak("Subha Voice AI agent started")

    while True:
        command = listen()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()