# SSW 540 - Assignment 12 - P12: Using Web API's
# Akshay Sunderwani

from math import radians, cos, sin, asin, sqrt
import googlemaps


def haversine(lon1, lat1, lon2, lat2):
    """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees).
        Source: http://gis.stackexchange.com/a/56589/15183
        """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    miles = int(km*(5/8))
    return miles

location2 = input('Enter your location (Must be a Non Hoboken location): ')

api_key_distance_matrix = 'AIzaSyBJCRh3eK2Y1LzGkTVsRNtWAfDmMN57Gy4'
api_key_geocoding_api = 'AIzaSyDKngZQLzgxyqBUXF-3jt_LP6RMbKGIjnQ'
api_key = 'AIzaSyCyiPScerc12oRQnBTTJCv1guCj2C0gExQ'

gmaps = googlemaps.Client(key=api_key_distance_matrix)

# Geocoding an address
geocode_result = gmaps.geocode('Hoboken, NJ')
geocode_result2 = gmaps.geocode(location2)

# # use the Google Maps API
# origins = []
# destinations = []
# origins.append ( str ( geocode_result[ 0 ][ 'geometry' ][ 'location' ]['lat'] ) + ' ' + str ( geocode_result[ 0 ][ 'geometry' ][ 'location' ]['lng'] ) )
# destinations.append ( str ( geocode_result2[ 0 ][ 'geometry' ][ 'location' ]['lat'] ) + ' ' + str ( geocode_result2[ 0 ][ 'geometry' ][ 'location' ]['lng'] ) )
# matrix = gmaps.distance_matrix(origins, destinations, units='imperial')
#
# if matrix['rows'][0]['elements'][0]['status'] != 'OK':
#     print('Distance between Hoboken, NJ and', location2, 'cannot be calculated. (BY GOOGLE GEOCODING)')
# else:
#     print('Distance between Hoboken, NJ and', location2, 'is :', matrix['rows'][0]['elements'][0]['distance']['text'], '. (BY GOOGLE GEOCODING)')

print('Distance between Hoboken, NJ and', location2, 'is :', haversine(geocode_result[ 0 ][ 'geometry' ][ 'location' ]['lng'],
                                                                         geocode_result[ 0 ][ 'geometry' ][ 'location' ]['lat'],
                                                                         geocode_result2[ 0 ][ 'geometry' ][
                                                                             'location' ][ 'lng' ],
                                                                         geocode_result2[ 0 ][ 'geometry' ][
                                                                             'location' ][ 'lat' ]), 'mile(s).')
