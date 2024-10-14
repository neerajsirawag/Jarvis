from buildin import KnowApps
from buildin import GoodMsg
# from func.Chat import Chat
from func.SpeakOffline import Speak
from func.ListenJs import Listen
from func.DataOnline import Online_Scrapper
from llm.ChatGpt import ChatGpt
# from llm.ChatGptColab import ChatGpt
# from func.OcrOnline import Ocr
# from func.OcrOffline import Ocr
from llm.Filter import Filter
from llm import ollama
import pygetwindow as gw
from time import sleep
import keyboard
import random

from Generation_Of_Images import *

# link = input("inter colab + https://f6e3-34-80-36-82.ngrok-free.app . No link enter 69 ->")
# if link == "69":
#     from llm.ChatGpt import ChatGpt
#     from func.OcrOffline import Ocr


import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

if __name__ == "__main__":
    while 1:
        Q = Listen()
        if Q is not None:
            QL = Q.lower()
            LQ=len(Q.split(" "))
            SQ=Q.split(" ")[0]
            EQ=Q.split(" ")[-1]
            
            CURRENT_APP = ""
            try:
                CURRENT_APP = gw.getActiveWindowTitle()
            except gw.PyGetWindowException:
                CURRENT_APP = ""
            CURRENT_APP_NAME = CURRENT_APP.split(" - ")[-1]
                         
               
            if CURRENT_APP_NAME in KnowApps:
                Func_ = KnowApps[CURRENT_APP_NAME]
                Output = Func_(QL)
                if Output != False:
                    keyboard.press_and_release(Output)
            
            # elif(SQ =="click" or (SQ == "double" and "click" in Q)) and LQ < 7:
            #     QL.replace("click","")
            #     QL.replace("on","")
            #     QL.replace("jarvis","")
            #     QL.replace("double","")
            #     A=Ocr(QL.strip())
            #     # A=Ocr(QL.strip(),url="https://112f-34-122-150-214.ngrok-free.app")
            #     Speak(A)
                
            # elif "jarvis" == SQ.lower:
            #     # code = ChatGpt(Q,"***just write complete code in python and don't provide any extra details***")
            #     code = Filter(code)
            #     exec(code)
            
            elif "shutdown"==SQ.lower():
                print(Fore.CYAN + "JARVIS : Shutting Down...\n")
                Speak("Shutting Down")
                break
            
            elif "jarvis" == SQ.lower():
                responce = ChatGpt(Q,"***just write complete code in python and don't provide any extra details***")
                # responce = ChatGpt(f"{Q} ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**")
                code = Filter(responce)
                if code != None:
                    if "from Generation_Of_Images import" in code or "import" not in code:
                        exec(code)
                    # elif "from func.Jukebox.YouTube import MusicPlayer" in code:
                    #     exec(code)
                    else:
                        Done = exec(code)
                        print(Done)
                        if Done:
                            Speak(random.choice(GoodMsg))
                        else:
                            for i in range(3):
                                with open(r"error.log", "r") as f:
                                    res = f.read()
                                    if res != "":
                                        ChatGpt(f"{res} /n" + "**fix this and write full code again. with different approach**")
                                        code = Filter(code)
                                        if code==None:
                                            break
                                        Done=exec(code)
                                        if Done==True:
                                            break
                                    else:
                                        break
                            # Speak("Sorry sir i Can't Do that")
                else:
                    done = exec(code)
                    if(done):
                        Speak(responce)
                
            else:
                web = Online_Scrapper(QL)
                if web != None:
                    print(Fore.CYAN + "JARVIS : " + web , flush = True )
                    Speak(web)
                # elif Chat(QL)[1] >= 0.99:
                #     print(Fore.CYAN + "JARVIS : " + Chat(QL)[0] , flush = True )
                #     Speak(Chat(QL)[0])
                else:
                    reply = ChatGpt(Q,"***reply like jarvis in less words and with some fun ***")
                    # ollama(Q + ". Try to reply in less words or in 1 line until you are asked to tell in brief")
                    # reply = ChatGpt(Q,"https://0ab5-34-125-50-20.ngrok-free.app")
                    Speak(reply)
                    