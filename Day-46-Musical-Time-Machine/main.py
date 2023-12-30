from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# travel_target = input("When do you want to travel to? Type the date in this format: YYYY-MM-DD ")
travel_target = "2019-01-05"
print(f"The appropriate question is, 'When the hell are they.' And they're in {travel_target}!")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{travel_target}/")
soup = BeautifulSoup(response.content, 'html.parser')
all_songs = soup.find_all(class_="o-chart-results-list-row-container")

songs = {}

for i in all_songs:
    title = i.h3.text.strip()
    author = i.find('ul', "lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")
    author = author.find('li').text
    author = author.replace(title, '').strip()
    songs[title] = author

# print(songs)


scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path='.cache'))

current_user_id = sp.current_user()['id']

uri_list = []
for song, artist in songs.items():
    try:
        result = sp.search(f'{song}, {artist}')
        uri_list.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"I couldn't find '{song}' by {artist} on Spotify.")

# for uri in uri_list:
#     print(uri)

playlist_id = sp.user_playlist_create(user=current_user_id, name=f"{travel_target} Billboard 100", public=True, description="Kopytko")['id']
sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
