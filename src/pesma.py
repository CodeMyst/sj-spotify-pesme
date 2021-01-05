class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Pesma:
    # duzina je u ms
    def __init__(self, ime, autor, album, godina, duzina):
        self.ime = ime
        self.autor = autor
        self.album = album
        self.godina = godina
        self.duzina = duzina

    # pretvara duzinu iz ms u minute:sekunde
    def vremeString(self):
        sekunde = int((self.duzina/1000)%60)
        minute = int((self.duzina/(1000*60))%60)

        return "{:02d}:{:02d}".format(minute, sekunde)

    # pretvori u string prema sledecem formatu:
    # ime
    # autor
    # album
    # vreme
    # prazan red
    # sve je u novom redu zbog lakseg ucitavanja, ako bi se koristio
    # neki separator (kao "-") moglo bi doci do greske pri ucitavanju
    # ako bi ime/autor/album sadrzali taj karakter
    def toLongString(self):
        return self.ime + "\n" + self.autor + "\n" + self.album + "\n" + \
            self.godina + "\n" + self.vremeString() + "\n\n"

    # lepsi prikaz pesme, prema sledecem formatu:
    # ime - autor - album - vreme
    def toShortString(self):
        ime = self.ime
        autor = self.autor
        album = self.album
        vreme = self.vremeString()

        if len(ime) > 37:
            ime = ime[:37] + "..."

        if len(autor) > 27:
            autor = autor[:27] + "..."

        if len(album) > 27:
            album = album[:27] + "..."

        return ("│  " + bcolors.OKBLUE + bcolors.BOLD + "{:<40}" + bcolors.ENDC + "  │   " + bcolors.OKBLUE + "{:<30}" + bcolors.ENDC + "   │   " + bcolors.OKBLUE + "{:<30}" + bcolors.ENDC + "   │  " + bcolors.FAIL + "{:<4}" + bcolors.ENDC + "  │  " + bcolors.FAIL + "{:<5}" + bcolors.ENDC + "  │") \
            .format(ime, autor, album, self.godina, vreme)
