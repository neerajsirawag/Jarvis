#pip install selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--use-fake-ui-for-media-stream")
# chrome_options.add_argument("--headless=new")
# driver = webdriver.Chrome(options=chrome_options)
# website = r"C:\Users\neera\OneDrive\Desktop\Extra\Jarvis\data\voice.html"

# driver.get(website)

# def Listen():
#     print("Listening...")
#     driver.find_element(by=By.ID, value='start').click()
#     while 1:
#         text = driver.find_element(by=By.ID,value='output').text
#         if text !="":
#             print("You said: " + text)
#             driver.find_element(by=By.ID,value='end').click()
#             return text

# while 1:
#     Listen()





#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from os import getcwd
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
# chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--headless")


# Set log level to suppress unnecessary logs
chrome_options.add_argument("--log-level=3")  # 3 is for errors only


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
website = f"{getcwd()}\\data\\voice.html"

driver.get(website)

def Listen():
    print()
    print(Fore.MAGENTA + "LISTENING... ")
    print()
    driver.get(website)
    driver.find_element(by=By.ID, value='start').click()
    while 1:
        text=driver.find_element(by=By.ID, value='output').text
        if text != "":
            print(Fore.YELLOW+"YOU: " + text)
            print()
            driver.find_element(by=By.ID, value='end').click()
            return text
        
if __name__=="__main__":
    while 1:
        Listen()
