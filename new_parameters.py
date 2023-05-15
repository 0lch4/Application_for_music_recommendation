import requests
import json
from conn import conn

response=conn()



def new_song(genre):
#wczytuje nowe dane utworu
    genre = genre.lower()
    if response.status_code == 200:
        access_token = response.json()['access_token']
        with open('results2.json') as f:
            new_data = json.load(f)
        #przypisuje wlasciwosci piosenki do zmiennych   
        tempo = new_data['tempo']
        loudness = new_data['loudness']
        valence = new_data['valence']
        energy = new_data['energy']
        time_signature = new_data['time_signature']
        mode = new_data['mode']
        key = new_data['key']
        danceability=new_data['danceability']
        speechiness=new_data['speechiness']
        instrumentalness=new_data['instrumentalness']
        popularity=new_data['popularity']

        headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"}
        #tworzy parametry ktore sa odczytywane przez strone
        params = {
            'limit': 3,
            'market': 'PL',
            'q': 'lang:pl',
            'seed_genres': genre,
            'target_tempo': tempo,
            'target_loudness': loudness,
            'target_valence': valence,
            'target_energy': energy,
            'target_time_signature': time_signature,
            'mode': mode,
            'key': key,
            'danceability':danceability,
            'speechiness':speechiness,
            'instrumentalness':instrumentalness,
            'popularity':popularity,
            'type': 'track',
        }
        #wysyla zapytanie o piosenke z podanymi parametrami
        response = requests.get("https://api.spotify.com/v1/recommendations", headers=headers, params=params, verify=True)
        if response.status_code == 200:
            results = response.json()["tracks"]
            #sprawdza czy taka piosenka istnieje
            if len(results) == 0:
                print("Nie znaleziono utworów dla podanych parametrów wyszukiwania.")
            else:
                i=1
                #wyswietla wyniki
                for track in results:
                    print(f"\nMiejsce {i}")
                    print(f"Utwór: {track['name']}")
                    print(f"Wykonawca: {track['artists'][0]['name']}")
                    print(f"Link do utworu: {track['external_urls']['spotify']}")
                    i+=1
        else:
            print(f"Nie udało się uzyskać wyników wyszukiwania. Kod statusu: {response.status_code}")
            
    return results