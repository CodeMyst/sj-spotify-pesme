import spotipy
import time
from pesma import Pesma
from playlista import Playlista
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

# ucitava sve playliste sa profila i vraca listu kao tuple (broj_playliste, ime_playliste)
def ucitaj_playliste():
    p = sp.current_user_playlists(limit=50)

    rez = [Playlista("0", "Liked Songs")]

    for i, item in enumerate(p["items"]):
        rez.append(Playlista(item["id"], item["name"]))

    return rez

# ucitava sve pesme iz izabranje playliste
# i cuva ih u fajl pesme.txt
# vraca listu svih pesama
def ucitaj_pesme(playlista):
    print("\nucitavanje pesama iz spotify-a iz playliste " + playlista.ime + "...")

    start_vreme = time.time()

    # otvori fajl za append
    f = open("pesme.txt", "a")

    # trenutni broj zahtevne strane
    broj_strane = 0

    pesme = []

    # ako je id liste 0, onda uzimamo "liked songs"
    if playlista.idp == "0":
        rez = sp.current_user_saved_tracks(LIMIT, broj_strane * LIMIT)
    else:
        rez = sp.playlist_items(playlista.idp, fields="items(track(duration_ms,name,artists(name),album(name,release_date)))", limit=LIMIT, offset=broj_strane * LIMIT, additional_types=["track"])

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
            # godina = pesma["album"]["release_date"][:4]
            godina = "2021"

            p = Pesma(ime, autor, album, godina, duz)

            f.write(p.toLongString())

            pesme.append(p)

        broj_strane += 1

        # ako je id liste 0, onda uzimamo "liked songs"
        # uzimanje sledece strane
        if playlista.idp == "0":
            rez = sp.current_user_saved_tracks(LIMIT, broj_strane * LIMIT)
        else:
            rez = sp.playlist_items(playlista.idp, fields="items(track(duration_ms,name,artists(name),album(name,release_date)))", limit=LIMIT, offset=broj_strane * LIMIT, additional_types=["track"])

    f.close()

    stop_vreme = time.time()

    t = stop_vreme - start_vreme
    print(str(len(pesme)) + " pesama ucitano za " + str(round(t, 2)) +
            " sekundi\n")

    return pesme
