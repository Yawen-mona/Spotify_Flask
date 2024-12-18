# 🎸This Week Music in London

This Flask web application generates a Spotify playlist featuring music tracks related to live events happening in London within a specified date range. Users can choose their date range(input start date and end date of your expected dates range), then click the Submit! button, and waiting for this web generating a Spotify playlist! The app integrates data from the Ticketmaster API to identify events and uses the Spotify API to create a curated playlist based on the event names.

## Features

1. **Interactive Date Selection**
   Users can input a start and end date for the events they want to discover.
2. **Event and Music Integration**
   Fetches live music events happening in London using the Ticketmaster API and searches for related songs on Spotify.
3. **Automatic Playlist Creation**
   Creates a public Spotify playlist with up to 30 songs and embeds it directly into the webpage.

## Prerequisites

1. **Python**
2. **Required Libraries**
   - `Flask`
   - `spotipy`
   - `requests`

## Code Overview

### Flask Application (`app.py`)

- Defines a route for the home page (`/`).
- Handles both `GET` (default date values) and `POST` (date form submission) requests.
- Uses the `get_playlist()` function to fetch events from Ticketmaster and create a Spotify playlist.

### HTML Template (`index.html`)

- Includes form elements for date selection.
- Displays an embedded Spotify iframe showcasing the generated playlist.

### Playlist Generation (`ticketmasterspotify.py`)

- **Ticketmaster API**:
  - Queries live music events in London within the given date range.
  - Filters events specific to London.
- **Spotify API**:
  - Searches for tracks related to event names.
  - Creates a public playlist and adds tracks to it.

### CSS Styles (`static/css/style.css`)

- Responsive design ensures usability on both desktop and mobile devices.
- Styled components include the date form, submit button, and Spotify iframe.



### Setup Instructions 

1. Clone the Repository Clone the project repository

2. Install the Python dependencies using `pip`:

   ```
   pip install -r requirements.txt
   ```

3. Set Up API Keys

​        You need to create two configuration files with your API keys:

​	**`APIexample.json` (Spotify API credentials)**: This file contains your Spotify application's client ID,    	client secret, redirect URI, and your Spotify username. The file should be structured as follows:

```
{
  "client_id": "your_spotify_client_id",
  "client_secret": "your_spotify_client_secret",
  "redirect": "your_spotify_redirect_uri",
  "username": "your_spotify_username"
}
```

​	**`ticketmaster_key.txt` (Ticketmaster API key)**: This file contains your Ticketmaster API key. 

​	You can obtain your key by registering on the Ticketmaster Developer Portal. The file should simply 	contain your key:

```
ticketmaster_api_key
```

## Example Workflow

1. **Input Dates**:
   Select a start date (`2024-11-18`) and an end date (`2024-11-25`).
2. **Fetch Events**:
   Ticketmaster API returns a list of music events happening in London during the specified range.
3. **Generate Playlist**:
   Spotify API searches for tracks related to the event names and creates a playlist with those tracks.
4. **View Playlist**:
   The generated playlist is embedded into the web page using a Spotify iframe.

## Error Handling

If there is an issue with fetching events or generating the playlist,  change the default start date and end date to your current dates to enable the app fetching events.
