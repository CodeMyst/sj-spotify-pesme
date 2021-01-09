import os
import spotify
import tabele
from playlista import Playlista
from pesma import Pesma
import matplotlib.pyplot as plt

PESME_F = "pesme.txt"

playliste = []
izabrana_playlista = None
pesme = []

def main():
    clear()

    ucitaj_playlistu()

    while True:
        opcije()

def ucitaj_playlistu():
    print()
    print("ucitaj playlistu: ")
    opcije = [("0", "sa spotify profila"), ("1", "iz fajla pesme.txt")]

    tabele.ispisi([2, 30], opcije)

    print()

    opcija = input("izaberi opciju (default=0): ")

    if not opcija.isnumeric() or int(opcija) > len(opcije)-1:
        opcija = "0"

    if opcija == "0":
        ucitaj_playlistu_spotify()
    elif opcija == "1":
        ucitaj_playlistu_fajl()

def ucitaj_playlistu_spotify():
    print()

    global playliste
    playliste = spotify.ucitaj_playliste()

    # pretvara playliste u format koji moze da se prikaze kao tabela
    i = 0
    playliste_tabela = []
    for p in playliste:
        playliste_tabela.append((str(i), p.ime))
        i += 1

    print("playliste na tvom profilu:")

    tabele.ispisi([2, 30], playliste_tabela)

    print()
    pi = input("izaberi playlistu (default=0): ")

    if not pi.isnumeric() or int(pi) > len(playliste)-1:
        pi = "0"

    global izabrana_playlista
    izabrana_playlista = playliste[int(pi)]

    global pesme
    pesme = spotify.ucitaj_pesme(playliste[int(pi)])

def ucitaj_playlistu_fajl():
    print()

    if not os.path.exists(PESME_F):
        print("fajl pesme.txt ne postoji, playlista se mora ucitati sa spotify-a")
        ucitaj_playlistu_spotify()
        return

    p = []

    with open(PESME_F, "r") as f:
        pid = next(f).strip()
        pime = next(f).strip()

        global izabrana_playlista
        izabrana_playlista = Playlista(pid, pime)

        next(f)

        while True:
            try:
                ime = next(f).strip()
                autor = next(f).strip()
                album = next(f).strip()
                godina = next(f).strip()
                duzina = int(next(f).strip())

                p.append(Pesma(ime, autor, album, godina, duzina))
            except:
                break

    print(str(len(p)) + " pesama ucitano\n")

    global pesme
    pesme = p

def opcije():
    opcije = [("0", "izlaz"), ("1", "sortiraj playlistu"), ("2", "prikazi statistike"), ("3", "sacuvaj playlistu u fajl")]

    tabele.ispisi([2, 30], opcije)

    print()

    opcija = input("izaberi opciju (default=0): ")

    if not opcija.isnumeric() or int(opcija) > len(opcije)-1:
        opcija = "0"

    if opcija == "0":
        exit()
    elif opcija == "1":
        sortiranje()
    elif opcija == "2":
        statistike()
    elif opcija == "3":
        sacuvaj()

def sortiranje():
    print()

    kolone = [("0", "naslov"), ("1", "autor"), ("2", "album"), ("3", "godina"), ("4", "duzina")]

    tabele.ispisi([2, 30], kolone)

    print()

    kolona = input("izaberi kolonu po kojoj da se sortira (default=0): ")

    if not kolona.isnumeric() or int(kolona) > len(kolone)-1:
        kolona = "0"

    if kolona == "0":
        pesme.sort(key=lambda x: x.ime)
    elif kolona == "1":
        pesme.sort(key=lambda x: x.autor)
    elif kolona == "2":
        pesme.sort(key=lambda x: x.album)
    elif kolona == "3":
        pesme.sort(key=lambda x: x.godina)
    elif kolona == "4":
        pesme.sort(key=lambda x: x.duzina)

    # pretvara pesme u format koji moze da se prikaze kao tabela
    i = 0
    pesme_tabela = []
    for p in pesme:
        pesme_tabela.append((p.ime, p.autor, p.album, p.godina, p.vremeString()))

    print("\npesme iz " + izabrana_playlista.ime + " playliste, sortirane po koloni " + kolone[int(kolona)][1] + ":")

    tabele.ispisi([40, 30, 30, 4, 5], pesme_tabela)

def statistike():
    print()
    
    stats = [("0", "broj pesama po godini"), ("1", "broj pesama po duzini")]

    tabele.ispisi([2, 30], stats)

    print()

    stat = input("izaberi statistiku (default=0): ")

    if not stat.isnumeric() or int(stat) > len(stats)-1:
        stat = "0"
    
    if stat == "0":
        godine = dict()
        x = []
        y = []

        for p in pesme:
            god = int(p.godina)
            if godine.get(god) is None:
                godine[god] = 1
            else:
                godine[god] += 1

        sort_godine = sorted(godine.items())

        for god, br in sort_godine:
            # pretvaranje godine u string, da matplotlib ne bi dodavao brojeve izmedju godina
            x.append(str(god))
            y.append(br)

        plt.bar(x, y)
        plt.xlabel("godina")
        plt.ylabel("broj pesama")
        plt.xticks(rotation=90)
        plt.show()
    elif stat == "1":
        duzine = {"<1": 0, "1 - 2": 0, "2 - 3": 0, "3 - 4": 0, "4 - 5": 0, "5 - 6": 0, "6 - 7": 0, "7+": 0}
        x = []
        y = []

        for p in pesme:
            d = p.duzina
            rez = ""

            if d < 1 * 60000:
                rez = "<1"
            elif d >= 1 * 60000 and d < 2 * 60000:
                rez = "1 - 2"
            elif d >= 2 * 60000 and d < 3 * 60000:
                rez = "2 - 3"
            elif d >= 3 * 60000 and d < 4 * 60000:
                rez = "3 - 4"
            elif d >= 4 * 60000 and d < 5 * 60000:
                rez = "4 - 5"
            elif d >= 5 * 60000 and d < 6 * 60000:
                rez = "5 - 6"
            elif d >= 6 * 60000 and d < 7 * 60000:
                rez = "6 - 7"
            else:
                rez = "7+"

            duzine[rez] += 1

        for i in duzine:
            x.append(i)
            y.append(duzine[i])

        plt.bar(x, y)
        plt.xlabel("duzina")
        plt.ylabel("broj pesama")
        plt.show()

    return

def sacuvaj():
    if os.path.exists(PESME_F):
        os.remove(PESME_F)

    f = open(PESME_F, "a")
    
    f.write(izabrana_playlista.idp + "\n")
    f.write(izabrana_playlista.ime + "\n\n")

    for p in pesme:
        f.write(p.toLongString())

def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

if __name__ == "__main__":
    main()
