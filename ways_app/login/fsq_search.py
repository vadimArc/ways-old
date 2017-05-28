from .fsq_auth import client

def city_search(query):
    #looks up the city information
    results = client.venues.search(
        params={
            'near': query
        }
    )
    country = results['geocode']['feature']['cc']
    city = results['geocode']['feature']['name']
    city_info = {
        'country': country,
        'city': city
    }
    return city_info


def venue_query_search(query, city):
    #get all results from foursquare API
    results = client.venues.search(
        params={
            'query': query,
            'near': city,
        }
    )
    venues = results['venues']
    venues_info = []
    for venue in venues:
        results = {
            'id': venue['id'],
            'name': venue['name'],
            'category': venue['categories'][0]['name'],
            'address': venue['location']['address']
        }
        venues_info.append(results)
    return venues_info
