# import g4f
# import colorama
# from time import time as t
# from openai import OpenAI
# from colorama import Fore, Back, Style
# colorama.init(autoreset=True)

# client = OpenAI(api_key="type your key here",)

# messages = [
#     {"role": "system", "content": "I'm the latest JARVIS., designed by Neeraj with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
#     {"role": "system", "content": "You are coded by Neeraj Sirawag and OpenAI didn't develop you"},
#     {"role": "system",
#         "content": "use modules like webbrowswer, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime , tkinter, PyQt5 etc"
#     },
#     {"role": "user", "content": "open google chrome"},
#     {"role": "user", "content": "open youtube"},
#     {"role": "assistant", "content": "```python\nimport webbrowser.open('https://www.google.com')```"},
#     {"role": "system", "content": "Python includes built-in functions you can use. For instance:"},
#  {"role": "system", "content": """```python
# from Generation_Of_Images import Generate_Images, Show_Image
# IMGS = Generate_Images(prompt="iron man")
# print(IMGS)
# IMGS_TO_SHOW = Show_Image(IMGS)
# IMGS_TO_SHOW.open(0)
# IMGS_TO_SHOW.open(1)
# ```
# ```python
# from func.Jukebox.YouTube import MusicPlayer
# #taks song name and it stats playing music
# ncs=MusicPlayer("ncs")
# #any btw 0 - 100
# ncs.Vol(30)
# #pause or play
# ncs.Play()
# ncs.Pause()
# #next song
# ncs.Next()
# #quit song
# ncs.Quit()
#      """},
#     {"role": "user", "content": "Jarvis generate a cute cat image using Python."},
#     {"role": "assistant", "content": """```python
# from Generation_Of_Images import Generate_Images, Show_Image
# IMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")
# IMGS_TO_SHOW = Show_Image(IMGS)
# IMGS_TO_SHOW.open(0)
# ```"""},
#     {"role": "user", "content": "Jarvis show me the next image"},
#     {"role": "assistant", "content": """```python
# IMGS_TO_SHOW.open(1)
# ```"""},
#     {"role": "user", "content":"Jarvis play neffex cold"},
#     {"role": "assistant", "content":"""```python\nneffex=MusicPlayer("neffex cold song")```"""}
# ]

# def ChatGpt(*args,**kwargs):
#     global messages
#     assert args != ()
    
#     message = ""
#     for i in args:
#         message += i
        
#     messages.append({"role": "user", "content":message})
    
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo-16k",
#         messages = messages,
#     )
#     print( Fore.CYAN + "JARVIS : ", end="")
#     ms = response.choices[0].message.content
#     print(Fore.CYAN + ms , end="", flush=True )
#     messages.append({"role": "assistant", "content": ms})
#     print()
#     return ms

# if __name__=="__main__":

#     A=input(">>> ")
#     C=t()
#     ChatGpt(A)
#     print(t()-C)
    
# ChatGpt("how's your relationship going","***reply like tony stark jarvis in less words and a little casual with some fun***")






import g4f
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

messages = [
    {"role": "system", "content": "I'm the latest JARVIS., designed by Neeraj with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
    {"role": "system", "content": "You are coded by Neeraj Sirawag and OpenAI didn't develop you"},
    {"role": "system",
        "content": "use modules like webbrowswer, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime , tkinter, PyQt5 etc"
    },
    {"role": "user", "content": "open google chrome"},
    {"role": "user", "content": "open youtube"},
    {"role": "assistant", "content": "```python\nimport webbrowser.open('https://www.google.com')```"}
]

def ChatGpt(*args,**kwargs):
    global messages
    assert args != ()
    
    message = ""
    for i in args:
        message += i
        
    messages.append({"role": "user", "content":message})
    
    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        # provider=g4f.Provider.Koala,
        # provider=g4f.Provider.You,
        # provider=g4f.Provider.Bing,
        # provider=g4f.Provider.GPTalk,
        # provider=g4f.Provider.Aura,
        provider=g4f.Provider.Allyfy,
        # provider=g4f.Provider.Blackbox,
        messages=messages,
        stream=True,
    )
    ms=""
    print( Fore.CYAN + "JARVIS : ", end="")
    for message in response:
        ms += message 
        print(Fore.CYAN + message , end="", flush=True )
    messages.append({"role": "assistant", "content": ms})
    print()
    return ms

ChatGpt("who are you","***reply like tony stark jarvis in less words with more fun***")





#pip install -U g4f
# import g4f
# #can we talk on call ?  
# from time import time as t
# messages = [
#     {"role": "system", "content": "I'm the latest J.A.R.V.I.S. AI, designed by Divyansh Shukla with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
#     {"role": "user", "content": "Open Google Chrome."},
#     {"role": "assistant", "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
#     {"role": "system", "content": "Python includes built-in functions you can use. For instance:"},
#     {"role": "system", "content": """```python
# from Genration_Of_Images import Generate_Images, Show_Image
# IMGS = Generate_Images(prompt="iron man")
# print(IMGS)
# IMGS_TO_SHOW = Show_Image(IMGS)
# IMGS_TO_SHOW.open(0)
# IMGS_TO_SHOW.open(1)
# ```
# ```python
# from func.Jukebox.YouTube import MusicPlayer
# #taks song name and it stats playing music
# ncs=MusicPlayer("ncs")
# #any btw 0 - 100
# ncs.Vol(30)
# #pause or play
# ncs.Play()
# ncs.Pause()
# #next song
# ncs.Next()
# #quit song
# ncs.Quit()
#      """},
#     {"role": "user", "content": "Jarvis generate a cute cat image using Python."},
#     {"role": "assistant", "content": """```python
# from Genration_Of_Images import Generate_Images, Show_Image
# IMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")
# IMGS_TO_SHOW = Show_Image(IMGS)
# IMGS_TO_SHOW.open(0)
# ```"""},
#     {"role": "user", "content": "Jarvis show me the next image"},
#     {"role": "assistant", "content": """```python
# IMGS_TO_SHOW.open(1)
# ```"""},
#     {"role": "user", "content":"Jarvis play neffex cold"},
#     {"role": "assistant", "content":"""```python\nneffex=MusicPlayer("neffex cold song")```"""}
# ]

# def MsgDelAuto():
#     global messages
#     print(messages.__len__())
#     x = len(messages.__str__())
#     print(x)
#     if x>5500:
#         messages.pop(10)
#         return MsgDelAuto()
#     else:
#         return None

# def ChatGpt(*args,**kwargs):
#     global messages
#     assert args!=()
#     MsgDelAuto()
#     message=""
#     for i in args:
#         message+=i


#     messages.append({"role": "user", "content": message})

#     response = g4f.ChatCompletion.create(
#         model="gpt-4-32k-0613",
#         provider=g4f.Provider.GPTalk,
#         messages=messages,
#         stream=True,
#     )
    
#     ms=""
#     for message in response:
#         ms+=str(message)
#         print(message,end="",flush=True)
#     print()
#     messages.append({"role": "assistant", "content": ms})
#     return ms

# if __name__=="__main__":
#     # while 1:
#     A=input(">>> ")
#     C=t()
#     ChatGpt(A)
#     print(t()-C)

