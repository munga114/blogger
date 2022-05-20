import urllib.request, json
from .auth.quotes import Quotes
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')

def get_quotes():
    response = urllib.request.get('http://quotes.stormconsultancy.co.uk/random.json')
    data=response.json()

    return data