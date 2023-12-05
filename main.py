import requests

search_url = "https://nominatim.openstreetmap.org"


def reverse(lat, lon):

    params_limit = {
        "format": 'json'
    }

    response = requests.get(url = search_url + "/reverse?lat=" + str(lat) + "&lon=" + str(lon), params = params_limit)
    result = response.json()
    if response.ok:
        return result['display_name']

def geocode(street, city, country):

    params_limit = {
        "street": street,
        "city": city,
        "country": country,
        "format": 'json'
    }

    response = requests.get(url = search_url + "/search", params = params_limit)
    result = response.json()
    if response.ok:
        return result[0]['lat'] + " " + result[0]['lon']
