import spotipy
import cred
from spotipy.oauth2 import SpotifyOAuth

# Authentication

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID,
                                               client_secret=cred.client_SECRET,
                                               redirect_uri=cred.redirect_url,
                                               scope=scope))

# Search for artist
name = input("Who do you want to listen to?")
result = sp.search(name)

# extract artist URI from search
artists_uri = result['tracks']['items'][0]['artists'][0]['uri']

# create list for song URIs
artist_song_uris = []

# Pull artist's top 10 tracks
all_top_tracks = sp.artist_top_tracks(artist_id=artists_uri)

# extract the track ID/uri for each track and add to a list as a string
for i, IDS in enumerate(all_top_tracks['tracks']):
    artist_song_uris.append(str(IDS['id']))

# creating the playlist
my_playlist = sp.user_playlist_create(user=sp.current_user()['id'],
                                      name=str(name) + "Top 10 Tracks",
                                      public=False)
# adding songs to playlist
sp.playlist_add_items(playlist_id=my_playlist['id'], items=artist_song_uris)
