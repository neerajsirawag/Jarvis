import requests


messages = [
    {"role": "system", "content": "I'm the latest JARVIS., designed by Neeraj with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
    {"role": "system", "content": "You are coded by Neeraj Sirawag and OpenAI didn't develop you"},
    {"role": "system",
        "content": "use modules like webbrowswer, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime , tkinter, PyQt5 etc"
    },
    {"role": "user", "content": "open google chrome"},
    {"role": "user", "content": "play on youtube"},
    {"role": "assistant", "content": "```python\nimport webbrowser.open('https://www.google.com')```"}
]

def ChatGpt(prompt, link):
    url = f'{link}/Gpt_Get_Data'  # Change the URL if the server is running on a different host

    # Define the JSON payload to send to the server
    json_payload = {
        "prompt": f"{prompt}",
        "model": "gpt-4-32k-0613"
    }

    try:
        with requests.post(url, json=json_payload, stream=True) as response:
            if response.status_code == 200:
                for chunk in response.iter_content(chunk_size=128, decode_unicode=True):
                    if chunk:
                        print(chunk)  # Print the response from the server
            else:
                print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed with an exception: {e}")

# print(use_gpt("write code to make snake game","https://f6e3-34-80-36-82.ngrok-free.app"))