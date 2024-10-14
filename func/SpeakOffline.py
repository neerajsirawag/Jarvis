import pyttsx3
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('rate',180)
engine.setProperty('voice',voices[1].id)

def Speak(*args, **kwargs):
    audio = ""
    for i in args:
        audio += str(i)
    # print(Fore.CYAN+"J.A.R.V.I.S.: "+audio,flush=True)
    engine.say(audio)
    engine.runAndWait()
    
# Speak("Hello! How are you...")



# from gtts import gTTS
# import pygame
# import colorama
# import os
# from colorama import Fore, Back, Style
# colorama.init(autoreset=True)

# def Speak(text, lang='en'):
#     audio = gTTS(text=text, lang=lang, slow=False)
#     audio.save("output.mp3")

#     pygame.mixer.init()
#     pygame.mixer.music.load("output.mp3")
#     print(Fore.CYAN + "J.A.R.V.I.S.: " + text, flush=True)
#     pygame.mixer.music.play()
#     pygame.mixer.music.set_volume(1.0)
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

# Speak("नमस्ते! मैं आपकी कैसे सहायता कर सकता हूँ?", lang='hi')


