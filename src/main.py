import os
import spotify
import tabele
from playlista import Playlista

playliste = []
izabrana_playlista = None
pesme = []

def main():
    clear()

    # todo: obrisi ovu liniju, samo za testiranje
    # todo: ako su pesme vec ucitane, prvo pitaj da li opet da ucita
    if os.path.exists("pesme.txt"):
        os.remove("pesme.txt")

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

    opcije()

def opcije():
    opcije = [("0", "izlaz"), ("1", "sortiraj playlistu"), ("2", "prikazi statistike")]

    tabele.ispisi([2, 30], opcije)

    print()

    opcija = input("izaberi opciju (default=0): ")

    if not opcija.isnumeric() or int(opcija) > 2:
        opcija = "0"

    if opcija == "0":
        exit()
    elif opcija == "1":
        sortiranje()
    elif opcija == "2":
        statistike()

def sortiranje():
    print()

    kolone = [("0", "naslov"), ("1", "autor"), ("2", "album"), ("3", "godina"), ("4", "duzina")]

    tabele.ispisi([2, 30], kolone)

    print()

    kolona = input("izaberi kolonu po kojoj da se sortira (default=0): ")

    if not kolona.isnumeric() or int(kolona) > 4:
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
    return

def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

if __name__ == "__main__":
    main()
