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

def get_flight(data):

    get_flight_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_flight_url) as url:
        get_flight_data = url.read()
        get_flight_response = json.loads(get_flight_data)

        flight_results = None

        if get_flight_response['data']:
            flight_results_list = get_flight_response['data']
            flight_results = process_results(flight_results_list)


    return flight_results

def process_results(flight_list):
   
    flight_results = []

    for flight in flight_list:
        source = flight.get('')
        destination = flight.get('')
        departure_date = flight.get('')
        arrival_date = flight.get('')
        seating_class = flight.get('')
        adults = flight.get('')
        children = flight.get('')
        infants = flight.get('')
        counter = flight.get('')

        if flight:
            flight_object = Flight(source, destination, departure_date, arrival_date, seating_class, adults, children, infants, ounter)
            flight_results.append(flight_object)

    return movie_results
        
        