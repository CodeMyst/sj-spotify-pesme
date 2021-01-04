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

        return "|  {:<40}  |   {:<30}   |   {:<30}   |  {:<4}  |  {:<5}  |" \
            .format(ime, autor, album, self.godina, vreme)
