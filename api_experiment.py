import os
import requests
import json
from dotenv import load_dotenv

# loading API key and secret
load_dotenv()

TM_API_KEY = os.getenv("TM_CONSUMER_KEY")

url = "https://app.ticketmaster.com/discovery/v2/events.json"
params = {
    "apikey": TM_API_KEY,
    "city": "Toronto",
    "size": 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    event = data["_embedded"]["events"][0]
    
    print(f"Success! Found an event:")
    print(f"Name: {event['name']}")
    print(f"ID:   {event['id']}")
else:
    print(f"Failed. Status Code: {response.status_code}")
    print(f"Response: {response.text}")