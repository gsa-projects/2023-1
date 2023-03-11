import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

cid = 'e22de1f6726f414382566eeb803d75b2'
secret = '089239a3305a45a58f133c804e7039b2'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# pprint(sp.categories(country="KR"))
result = sp.search("newjeans", limit=1, type="artist")
pprint(result)