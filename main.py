import csv
import requests
from var import *


def extract_data(api_url, url_headers):
    return requests.get(url=api_url, headers=url_headers)


def return_json(response):
    res = response.json()
    artist_name = res['tracks'][0]['album']['artists'][0]['name']
    song_name = res['tracks'][0]['album']['name']
    release_date = res['tracks'][0]['album']['release_date']
    top_song = res['tracks'][0]['name']
    return artist_name, song_name, release_date, top_song


with open('Db.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Artist Name", "Song Name", "Release Date", "Top Song"])

    artists_dict = {"Queen": ID1,
                    "Biggie": ID2,
                    "Boris Brejcha": ID3,
                    "Nirvana": ID4,
                    "The Neighbourhood": ID5
                    }
    for i in artists_dict.values():
        url = f"https://api.spotify.com/v1/artists/{i}/top-tracks?market=ES"

        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": f"Bearer {token}"}
        r = extract_data(api_url=url, url_headers=headers)

        row = return_json(r)
        writer.writerow(row)
