import urllib.request,json
from .models import Flight
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

api_key = None

base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['FLIGHT_API_KEY']
    base_url = app.config['FLIGHT_API_BASE_URL']

def get_flight(category):
    get_flight_url = base_url.format(category,api_key)

    