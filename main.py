import requests
import json
import os

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=1d014953cb6849ed9ad123722230411&q={city}"

r = requests.get(url)
# print(r.text)
# print(type(r.text))
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

os.system(f'''"PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{f'The current weather in {city} is {w} degrees'}');"''')