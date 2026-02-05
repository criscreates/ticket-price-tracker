import os
import requests
import json
from dotenv import load_dotenv

# loading API key and secret
load_dotenv()

TM_API_KEY = os.getenv("TICKETMASTER_API_KEY")