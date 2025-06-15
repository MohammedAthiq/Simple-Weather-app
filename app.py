import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

city = input("Enter city name bruh: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"Temperature in {city}: {temperature}°C")
    print(f"Weather Condition: {description}")
else:
    print("City not found. Please check the spelling.")