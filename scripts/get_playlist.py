# input the playlist_id and name of the desired o/p csv dump.
# This program creates a csv dump with the songs from that playlist from spotify.

import spotipy
import os
import numpy as np
import pandas as pd
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

CLIENT_ID = '74244a4b45b9486e8144ab7c961e3d73'
SPOTIPY_CLIENT_SECRET = 'cfaf3d7791a3486987bb2542ff403bfd'

os.environ['SPOTIPY_CLIENT_ID'] = CLIENT_ID
os.environ['SPOTIPY_CLIENT_SECRET'] = SPOTIPY_CLIENT_SECRET
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:7777/callback'

def fetch_playlist_features(creator, playlist_id):
    playlist_features_list = ['artist', 'album', 'track_name', 'track_id', 'popularity', 'danceability',
                              'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                              'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']
    
    playlist_df = pd.DataFrame(columns = playlist_features_list)
    playlist_features = {}
    
    i = 0
    playlist = []
    while True:
        if(len(sp_client.user_playlist_tracks(user, playlist_id, offset = i*100)['items']) != 0 ):
            playlist.append(sp_client.user_playlist_tracks(user, playlist_id, 
                                                           offset = i*100)['items'])
            i+=1
        else:
            break
    for i in range(len(playlist)):
        for track in playlist[i]:
            playlist_features['artist'] = track['track']['album']['artists'][0]['name']
            playlist_features['album'] = track['track']['album']['name']
            playlist_features['track_name'] = track['track']['name']
            playlist_features['track_id'] = track['track']['id']
            playlist_features['popularity'] = track['track']['popularity']
            # Get audio features
            audio_features = sp_client.audio_features(playlist_features['track_id'])[0]
            for feature in playlist_features_list[5:]:
                playlist_features[feature] = audio_features[feature]
            #concat the dfs
            track_df = pd.DataFrame(playlist_features, index = [0])
            playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)
    return playlist_df

if __name__ == '__main__':
    discover = 'spotify:playlist:37i9dQZEVXcUNzDN8qIGmk'
    discover = input("Input the playlist id : ")
    user = 'spotify'
    auth_manager = SpotifyClientCredentials()
    scope = 'playlist-read-private, user-library-read'
    sp_client = spotipy.Spotify(auth_manager = SpotifyOAuth(scope = scope, username = 'shivakumar'))
    discover_df = fetch_playlist_features(user, discover)
    op_csv = input("Name of the o/p csv: ")
    discover_df.to_csv('dataset/{}.csv'.format(op_csv), index = False)