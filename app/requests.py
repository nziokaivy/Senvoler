import urllib.request,json



api_key = None

base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['FLIGHT_API_KEY']
    base_url = app.config['FLIGHT_API_BASE_URL']

def get_flight(places):

    get_flight_url = 'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0?api_key={}&inboundDate={}&cabinClass={}&children={}&infants={}&country={}&currency={}&locale={}'.format(places,api_key)

    with urllib.request.urlopen(get_flight_url) as url:
        get_flight_data = url.read()
        get_flight_response = json.loads(get_flight_data)

        flight_results = None

        if get_flight_response['places']:
            flight_results_list = get_flight_response['places']
            flight_results = process_results(flight_results_list)
            
            print(flight_results)


   
        
        