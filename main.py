import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

listener = sr.Recognizer()
player = pyttsx3.init()


def listen():
    with sr.Microphone() as input_device:
        print("I am Ready,Listening...")
        voice_content = listener.listen(input_device)
        text_command = listener.recognize_google(voice_content)
        print("You said: " + text_command)
    return text_command


def talk(text):
    player.say(text)
    player.runAndWait()

def run_voice_bot():
    command = listen()
    if "wh is" in command:
        command = command.replace("who is", "")
        info = wikipedia.summary(command, 5)
        talk(info)
    elif "play" in command:
        command = command.replace("play", "")
        pywhatkit.playonyt(command)
    else:
        talk("Sorry,I could not understand what are you looking for")


run_voice_bot()
