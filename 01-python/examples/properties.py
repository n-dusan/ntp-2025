# 2. Properties
# izvedeni atributi

# Da li u Python-u imamo prava pristupa?
# Kako se uglavnom realizuju
# Evo jedan mehanizam koji bi to mogao omoguciti (u neku ruku)

class Osoba:
    def __init__(self, ime="", prezime=""):
        self.ime = ime
        self.prezime = prezime

    @property
    def ime_i_prezime(self):
        return "%s %s" % (self.ime, self.prezime)

    @ime_i_prezime.setter
    def ime_i_prezime(self, tekst):
        delovi = tekst.strip().split()
        if len(delovi) != 2:
            raise ValueError("dozvoljeno je uneti samo ime i prezime")
        self.ime, self.prezime = delovi[0].strip(), delovi[1].strip()


def main():
    o = Osoba("pera", "peric")
    print(o.ime_i_prezime)
    o.ime_i_prezime = "Mika Mikic"
    print(o.ime_i_prezime)
    try:
        o.ime_i_prezime = "Zika Zike Zikic"
    except ValueError:
        print("Los format")


if __name__ == '__main__':
    main()
