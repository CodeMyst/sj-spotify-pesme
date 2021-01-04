import spotipy
import time
from pesma import Pesma
from spotipy.oauth2 import SpotifyOAuth

# limit koliko pesama moze API da uzme iz jednog zahteva,
# pomocu "paging"-a, se preko vise zahteva uzimaju sve pesme
LIMIT = 20

# todo: ucitaj client_id i client_secret iz configa
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="f342b5e0b3704ee5bd7263ab93af4aa8",
    client_secret="4d0abacfce5f481cad3418393b533b8e",
    redirect_uri="http://localhost:5000/spotify-callback",
    scope="user-library-read"))

# ucitava sve pesme is korisnikove "Liked Songs" playliste,
# i cuva ih u fajl pesme.txt
# vraca listu svih pesama
def ucitaj_pesme():
    print("ucitavanje pesama iz spotify-a...")

    start_vreme = time.time()

    # otvori fajl za append
    f = open("pesme.txt", "a")

    # trenutni broj zahtevne strane
    broj_strane = 0

    pesme = []

    rez = sp.current_user_saved_tracks(LIMIT, broj_strane * LIMIT)

    # dok god trenutna strana ima pesama, uzmi sve pesme sa strane
    # i ispisi ih u fajl
    while len(rez["items"]) > 0:
        # za svaku pesmu sa strane
        for i, item in enumerate(rez["items"]):
            pesma = item["track"]

            # duzina pesme u ms
            duz = pesma["duration_ms"]

            ime = pesma["name"]
            # pesma moze imati vise autora, uzmi samo prvog
            autor = pesma["artists"][0]["name"]
            album = pesma["album"]["name"]
            godina = pesma["album"]["release_date"][:4]

            p = Pesma(ime, autor, album, godina, duz)

            f.write(p.toLongString())

            pesme.append(p)

        broj_strane += 1
        rez = sp.current_user_saved_tracks(LIMIT, broj_strane * LIMIT)

    f.close()

    stop_vreme = time.time()

    t = stop_vreme - start_vreme
    print(str(len(pesme)) + " pesama ucitano za " + str(round(t, 2)) +
            " sekundi")

    return pesme
