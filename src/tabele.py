PLAVA = '\033[94m'
CRVENA = '\033[91m'
BELA = '\033[0m'
BOLD = '\033[1m'

# ispisuje lepo formatiranu tabelu
# duz_kolone - lista koja sadrzi maksimalne duzine kolona
# vrednosti - lista koja sadrzi liste koje predstavljaju vrednosti tabele, svi elementi liste moraju biti string
def ispisi(duz_kolone, vrednosti):
    print("┌", end="")

    # ispisi pocetak tabele
    i = 0
    for kol in duz_kolone:
        print("─" * (kol+4), end="")

        if i != len(duz_kolone)-1:
            print("┬", end="")

        i += 1

    print("┐")

    # ispisi vrednosti tabele
    for vrednost in vrednosti:
        print("│  ", end="")
        j = 0
        for v in vrednost:
            # sve vrednosti su plave boje, osim ako je to prva kolona, tad je vrednost crvena i bold
            boja = PLAVA
            if j == 0:
                boja = CRVENA + BOLD

            # ako je vrednost duza od duzine kolone, skrati string i dodaj "..."
            if len(v) > duz_kolone[j]:
                s = duz_kolone[j]-3
                v = v[:s] + "..."

            print(boja + ("{:<" + str(duz_kolone[j]) + "}").format(v) + BELA + "  │  ", end="")
            j += 1
        print("")

    print("└", end="")

    # ispisi kraj tabele
    i = 0
    for kol in duz_kolone:
        print("─" * (kol+4), end="")

        if i != len(duz_kolone)-1:
            print("┴", end="")

        i += 1

    print("┘")
