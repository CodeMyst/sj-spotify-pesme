import os
import spotify

def main():
    # todo: obrisi ovu liniju, samo za testiranje
    if os.path.exists("pesme.txt"):
        os.remove("pesme.txt")

    spotify.ucitaj_pesme()

if __name__ == "__main__":
    main()
