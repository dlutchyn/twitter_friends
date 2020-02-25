import twitter
import folium
import geocoder

consumer_key = 'AzK4GnL4Juvcdpqc34QKT8jhp'
consumer_secret = 'EFQmiovJUaEWGHDILOswNOxBHKDMiNpdJzVj3gLiPkVPM3nMtl'
access_token = '993554105653235712-EeTMoNmQywvwDSR5RU4lv6F97aT3uwh'
access_secret = 'ALvxaUdZqE2Km1FYSQS8dzFeHipZOSaTMzEAMpN09vJpY'


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_secret)


def get_friends(screen_name: str) -> list:
    '''
    (str) -> (list)
    Returns a list if tuples with the name and the location of
    given user's friends.
    '''
    friends = api.GetFriends(screen_name=screen_name)
    return [(friend.name, friend.location) for friend in friends]


def get_friend_geolocation(friend: list) -> tuple:
    '''
    (list(tuple)) -> (tuple)
    Returns the coordinates of the chosen friend.
    '''
    try:
        location = geocoder.osm(friend[1]).osm
        coordinates = (location['x'], location['y'])
        return coordinates
    except TypeError:
        return None


def draw_map(friends: str):
    '''
    (str) -> html file
    Draws markers on the map that show friends of the given user.
    '''
    map = folium.Map(location=[49.8397, 24.0297], Zoom_start=2)
    fg = folium.FeatureGroup(name="Friends_map")
    for friend in friends:
        try:
            geolocation = get_friend_geolocation(friend)
            print(geolocation)
            lt = geolocation[0]
            ln = geolocation[1]
            location = friend[1]
            name = friend[0]
            fg.add_child(folium.Marker(location=[ln, lt],
                                       radius=5,
                                       popup=f'name: {name}\nlocation:{location}',
                                       fill_color='green',
                                       color='green',
                                       fill_opacity=0.5))
        except ValueError:
            continue
        except TypeError:
            continue
    map.add_child(fg)
    map.save('templates/Friends_map.html')


# if __name__ == "__main__":
#     name = input("Type user's name: ")
#     friends = get_friends(name)
#     print(friends)
#     draw_map(friends)
