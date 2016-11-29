# SSW 540 - Assignment 12 - P12: Using Web API's
# Akshay Sunderwani

import googlemaps

location2 = input('Enter your location (Must be a Non Hoboken location): ')

api_key_distance_matrix = 'AIzaSyBJCRh3eK2Y1LzGkTVsRNtWAfDmMN57Gy4'
api_key_geocoding_api = 'AIzaSyDKngZQLzgxyqBUXF-3jt_LP6RMbKGIjnQ'
api_key = 'AIzaSyCyiPScerc12oRQnBTTJCv1guCj2C0gExQ'

gmaps = googlemaps.Client(key=api_key_distance_matrix)

# Geocoding an address
geocode_result = gmaps.geocode('Hoboken, NJ')
geocode_result2 = gmaps.geocode(location2)

# use the Google Maps API
origins = []
destinations = []
origins.append ( str ( geocode_result[ 0 ][ 'geometry' ][ 'location' ]['lat'] ) + ' ' + str ( geocode_result[ 0 ][ 'geometry' ][ 'location' ]['lng'] ) )
destinations.append ( str ( geocode_result2[ 0 ][ 'geometry' ][ 'location' ]['lat'] ) + ' ' + str ( geocode_result2[ 0 ][ 'geometry' ][ 'location' ]['lng'] ) )
matrix = gmaps.distance_matrix(origins, destinations, units='imperial')

if matrix['rows'][0]['elements'][0]['status'] != 'OK':
    print('Distance between Hoboken, NJ and', location2, 'cannot be calculated.')
else:
    print('Distance between Hoboken, NJ and', location2, 'is :', matrix['rows'][0]['elements'][0]['distance']['text'])
