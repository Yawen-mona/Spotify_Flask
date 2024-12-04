from flask import Flask, render_template, request
from ticketmasterspotify import get_playlist

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Default values for GET request
    user_start_date = '2024-11-18'
    user_end_date = '2024-11-25'

    # Update values for POST request
    if request.method == 'POST':
        user_start_date = request.form['req_start_date']
        user_end_date = request.form['req_end_date']

    start_date = f"{user_start_date}T00:00:00Z"
    end_date = f"{user_end_date}T00:00:00Z"
    my_songs = get_playlist(start_date, end_date)

    # Check if an error message was returned
    if isinstance(my_songs, str) and "Error" in my_songs:
        return render_template(
            'index.html',
            error_message=my_songs,
            start_date=user_start_date,
            end_date=user_end_date
        )

    return render_template('index.html', playlist_id=my_songs, start_date=user_start_date, end_date=user_end_date)

