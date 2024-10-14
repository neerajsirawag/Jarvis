import requests
from bs4 import BeautifulSoup

# classes=["hgKElc","kno-rdesc","zCubwf","LTKOO sY7ric", "Z0LcW","gsrt vk_bk FzvWSb YwPhnf","pclqee","IZ6rdc","O5uR6d LTKOO","vlzY6d","webanswers-webanswers_table_webanswers-table","dDoNo ikb4Bb gsrt","sXLaOe","LWkfke", "Ab33Nc","qv3Wpe","SPZz6b","s6JM6d"]
# classes=["zCubwf","hgKElc","LTKOO sY7ric","Z0LcW","gsrt vk_bk FzvWSb YwPhnf","pclqee","tw-Data-text tw-text-small tw-ta","IZ6rdc","O5uR6d LTKOO","vlzY6d","webanswers-webanswers_table__webanswers-table","dDoNo ikb4Bb gsrt","sXLaOe","LWkfKe","VQF4g","qv3Wpe","kno-rdesc"]

classes=["g7W7Ed","zCubwf","hgKElc","LTKOO sY7ric","Z0LcW","gsrt vk_bk FzvWSb YwPhnf","pclqee","tw-Data-text tw-text-small tw-ta","IZ6rdc","O5uR6d LTKOO","vlzY6d","webanswers-webanswers_table__webanswers-table","dDoNo ikb4Bb gsrt","sXLaOe","LWkfKe","VQF4g","qv3Wpe","kno-rdesc"]

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

def Online_Scrapper(query,PRINT=False):
    query=query.replace(" + "," plus ")
    query=query.replace(" - "," minus ")
    
    URL = f"https://www.google.co.in/search?q={query}"
    headers = {'User-Agent':useragent}
    
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    
    for i in classes:
        try:
            result = soup.find(class_=i).get_text(" ")
            if PRINT:
                print("By class: ",i)
            return result
        except Exception:
            pass
    return None 

# print(Online_Scrapper("weather un gharuan",True))










# #pip install requests
# #pip install bs4
# #pip install selenium

# import time
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "Z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "IZ6rdc", "O5uR6d LTKOO",
#            "vlzY6d", "webanswers-webanswers_table_webanswers-table", "dDoNo ikb4Bb gsrt", "sXLaOe", "LWkfke", "Ab33Nc",
#            "qv3Wpe", "SPZz6b", "s6JM6d"]

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# def Online_Scrapper(query, PRINT=False):
#     query = query.replace(" + ", " plus ")
#     query = query.replace(" - ", " minus ")

#     # Using headless browser to render JavaScript content
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#     chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

#     driver = webdriver.Chrome(options=chrome_options)
#     URL = f"https://www.google.co.in/search?q={query}"

#     driver.get(URL)
#     time.sleep(2)  # Allow time for dynamic content to load

#     page_source = driver.page_source
#     soup = BeautifulSoup(page_source, 'html.parser')

#     for i in classes:
#         try:
#             result = soup.find(class_=i).get_text()
#             if PRINT:
#                 print("by class ", i)
#             return result
#         except Exception:
#             pass

#     driver.quit()  # Close the browser
#     return "no idea about that"

# print(__about__("Powershell", True))


