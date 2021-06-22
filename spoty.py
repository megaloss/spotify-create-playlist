import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import random

scope = 'playlist-modify-public'
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
print(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope=scope))


def show_playlists():
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])


def create_playlist(name, description=''):
    user_id = sp.me()['id']
    result = sp.user_playlist_create(user_id, name)
    return result


def add_track(playlist_id, tracks):
    sp.playlist_add_items(playlist_id, tracks)


tracks = []
with open('/home/yurick/Downloads/playlist.txt', 'r') as f:
    for line in f:
        tracks.append(line.strip())
random.shuffle(tracks)
print(tracks[:10])

playlist_id = create_playlist('Auto-generated')['id']
print('created playlist with id', playlist_id)
add_track(playlist_id, tracks[:100])
