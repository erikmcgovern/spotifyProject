import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import os

load_dotenv()

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:5000'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-top-read'
    )
)



st.set_page_config(page_title='Spotify Song Analysis', page_icon='musical_note')
st.title('Analysis for your Top Songs')
st.write('Discover insights about your Spotify listening habits.')

top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')
track_ids = [track['id'] for track in top_tracks['items']]
audio_features = sp.audio_features(track_ids)

df = pd.DataFrame(audio_features)
df['track_name'] = [track['name'] for track in top_tracks['items']]
df = df[['track_name', 'danceability', 'energy', 'valence']]
df.set_index('track_name', inplace=True)

st.subheader('Audio Features for Top Tracks')
st.bar_chart(df, height=500)


print('test')










