import os
import spotify

def main():
    # todo: obrisi ovu liniju, samo za testiranje
    # todo: ako su pesme vec ucitane, prvo pitaj da li opet da ucita
    if os.path.exists("pesme.txt"):
        os.remove("pesme.txt")

    pesme = spotify.ucitaj_pesme()

    print("-" * 139)

    for pesma in pesme:
        print(pesma.toShortString())

    print("-" * 139)

if __name__ == "__main__":
    main()
