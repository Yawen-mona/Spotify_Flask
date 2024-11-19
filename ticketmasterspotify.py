import spotipy
import json
import webbrowser
import urllib.request
import spotipy.util as util
import requests
import collections

with open('ticketmaster_key.txt','r') as key_file:
    ticketmaster_key = key_file.read()

with open('APIexample.json', 'r') as spotify_file:
    tokens = json.load(spotify_file)

my_client_id = tokens['client_id']
my_client_secret = tokens['client_secret']
redirectURI = tokens['redirect']
username = tokens['username']

scope = "user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public"
token = util.prompt_for_user_token(username, scope, client_id=my_client_id, client_secret=my_client_secret, redirect_uri=redirectURI)

# we are creating an object (sp) that can interact with the Spotify API
sp = spotipy.Spotify(auth=token)


def get_playlist(start_date, end_date):
    encoded_start_date = urllib.parse.quote(start_date)
    encoded_end_date = urllib.parse.quote(end_date)
    dma_id = 601
    url = (f"https://app.ticketmaster.com/discovery/v2/events.json?"
       f"classificationName=music&countryCode=GB&"
       f"startDateTime={encoded_start_date}&endDateTime={encoded_end_date}&"
       f"dmaId={dma_id}&size=200&apikey={ticketmaster_key}")

    
    request = urllib.request.Request(url) 
    response = urllib.request.urlopen(request)
    
    events = json.loads(response.read())
    
    songs_for_playlist = []
    
    if '_embedded' in events and 'events' in events['_embedded']:
        events_list = events['_embedded']['events']
    
        # Extract event names where the venue is in London
        london_events_info = [
            event['name']  # Collecting the event name only
            for event in events_list
            if 'name' in event and 'London' in event['_embedded']['venues'][0]['city']['name']
         ]




    for event in london_events_info:
        search_results = sp.search(q=event, type="track", limit=1)
        if search_results['tracks']['items']:
            song_uri = search_results['tracks']['items'][0]['uri']
            if song_uri not in songs_for_playlist:  # Avoid duplicates
                songs_for_playlist.append(song_uri)

    if len(songs_for_playlist) > 30:
        songs_for_playlist = songs_for_playlist[:30]


    my_playlist = sp.user_playlist_create(user=username, name="This Week London Music", public=True, description="Songs for this week concert and event music in L")
    sp.user_playlist_add_tracks(username, my_playlist['id'], songs_for_playlist)
    return my_playlist['id']