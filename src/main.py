import os
import spotify
import tabele

def main():
    print("")

    # todo: obrisi ovu liniju, samo za testiranje
    # todo: ako su pesme vec ucitane, prvo pitaj da li opet da ucita
    if os.path.exists("pesme.txt"):
        os.remove("pesme.txt")

    playliste = spotify.ucitaj_playliste()

    # pretvara playliste u format koji moze da se prikaze kao tabela
    i = 0
    playliste_tabela = []
    for p in playliste:
        playliste_tabela.append((str(i), p.ime))
        i += 1

    print("playliste na tvom profilu:")

    tabele.ispisi([2, 30], playliste_tabela)

    print("")
    pi = input("izaberi playlistu (default=0): ")

    if not pi.isnumeric() or int(pi) > len(playliste)-1:
        pi = "0"

    pesme = spotify.ucitaj_pesme(playliste[int(pi)])

    # pretvara pesme u format koji moze da se prikaze kao tabel
    i = 0
    pesme_tabela = []
    for p in pesme:
        pesme_tabela.append((p.ime, p.autor, p.album, p.godina, p.vremeString()))

    print("pesme iz " + playliste[int(pi)].ime + " playliste:")

    tabele.ispisi([40, 30, 30, 4, 5], pesme_tabela)

    # print("┌" + "─"*44 + "┬" + "─"*36 + "┬" + "─"*36 + "┬" + "─"*8 + "┬" + "─"*9 + "┐")

    # i = 0
    # for pesma in pesme[:10]:
    #     print(pesma.toShortString())
    #     if i != 9:
    #         print("├" + "─"*44 + "┼" + "─"*36 + "┼" + "─"*36 + "┼" + "─"*8 + "┼" + "─"*9 + "┤")
    #     i += 1

    # print("└" + "─"*44 + "┴" + "─"*36 + "┴" + "─"*36 + "┴" + "─"*8 + "┴" + "─"*9 + "┘")

if __name__ == "__main__":
    main()
