from .fsq_auth import client
from login.models import Profile, Cities, Lists, Cache, Places

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
            'address': venue['location']['address'],

        }
        venues_info.append(results)
    return venues_info

def venue_save(venue_id, city_name):
    venue = client.venues(venue_id)['venue']
    venue_info = Places(
        name = venue['name'],
        venue_id = venue['id'],
        category = venue['categories'][0]['name'],
        category_id = venue['categories'][0]['id'],
        address = venue['location']['address'],
        lat = venue['location']['lat'],
        lng = venue['location']['lng']
    )
    venue_info.save()
    return venue_info
