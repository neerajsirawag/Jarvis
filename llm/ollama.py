import subprocess
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def run_ollama(command):
    print( Fore.CYAN + "JARVIS : ")
    subprocess.run(f"ollama run llama3.2 {command}")

if __name__ == "__main__":
    while(1):
        command = input(Fore.YELLOW + "You: ")
        if(command.lower() == "shutdown"):
            break
        run_ollama(command +". reply like jarvis in less words and with some fun.")