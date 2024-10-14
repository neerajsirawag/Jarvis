import requests
from PIL import ImageGrab
import io
from pyautogui import click,sleep

def Ocr(st,url:str,double_click:bool=False):
    #take screenshot
    screenshot = ImageGrab.grab()

    #Connect the image to bytes
    image_bytes = io.BytesIO()
    screenshot.save(image_bytes, format="PNG")
    image_bytes.seek(0)

    #create a dictionary with the form data
    if double_click:
        payload = {
            "search_string": st,
            "double_click": "on"
        }
        files = {'image': image_bytes}
    else :
        payload = {
            "search_string": st,
            "double_click": "off"
        }
        files = {'image': image_bytes}
        
    #Send a POST request to the Flask application
    response = requests.post(f"{url}/imgs",files=files, data=payload)
    screenshot.close()
    print(response.json())
    
    if 'error' in response.json():
        return f"No button found name {st}"
    else:
        response_data = response.json()
        print(response_data["time"])
        point = response_data["point"]
        if double_click:
            click(point)
            sleep(0.30)
            click(point)
            return f"button found name {st} clicking on it"
        else:
            click(point)
            return f"button found name {st} clicking on it"

# print(Ocr("main.py","https://f6e3-34-80-36-82.ngrok-free.app",False))