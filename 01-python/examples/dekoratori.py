import time
import datetime


# 4. Dekoratori

# Funkcije su first-class objekti u Pythonu

def dobro_jutro(ime):
    return "Dobro jutro: %s" % ime


def dobar_dan(ime):
    return "Dobar dan: %s" % ime


def dobro_vece(ime):
    return "Dobro vece: %s" % ime


# funkcija se moze proslediti kao parametar, tj. bilo koji callable objekat
def pozdrav(func_pozdrav, ime):
    pozdrav = func_pozdrav(ime)
    print("Ovo je pozdrav koji cemo uputiti: %s" % pozdrav)


def funkcije_kao_first_class_objekti():
    pozdrav(dobro_jutro, "Mika")
    pozdrav(dobar_dan, "Zika")
    pozdrav(dobro_vece, "Pera")


# python podrzava unutrasnje funkcije i leksicko zatvorenje (lexical closure)
def pozdrav_vreme_dekorisanje(func):
    import datetime
    vreme = datetime.datetime.now()

    # *args, **kwargs odgovaraju argumentima funkcije
    # ne razmisljamo o njima, prosto ih sve prosledimo
    # Da ne koristimo generalizaciju pomocu *args, i **kwargs,
    # onda bismo morali menjati dekorator pri promeni potpisa funkcije koju smo generisali.
    # Sta ako dekorisemo funkcije sa razlicitim brojem parametara
    def wrapper(*args, **kwargs):
        print("Pocinje wrapper funkcije")
        ret = func(*args, **kwargs)
        print("Zavrsava se wrapper funkcija")
        return "%s, vreme dekorisanja funkcije: %s, vreme poziva dekorisane funkcije: %s" \
               % (ret, vreme, datetime.datetime.now())

    # funkcija se moze vratiti kao parametar
    return wrapper


def dekoratori_rucno():
    print(">>> Rucno simuliranje dekorator ponasanja")
    print(datetime.datetime.now())
    # mora se funkcija rucno dekorisati
    poz_dobro_jutro_func = pozdrav_vreme_dekorisanje(dobro_jutro)
    poz_dobar_dan_func = pozdrav_vreme_dekorisanje(dobar_dan)
    poz_dobro_vece_func = pozdrav_vreme_dekorisanje(dobro_vece)
    time.sleep(3)
    print(datetime.datetime.now())
    print(poz_dobro_jutro_func("Mika"))
    time.sleep(1)
    print(poz_dobar_dan_func("Zika"))
    time.sleep(1)
    print(poz_dobro_vece_func("Pera"))


# dekorator koji ima parametar
def uvuci(broj_razmaka=20):
    # dekorator
    uvlacenje = " " * broj_razmaka

    def uvuci_decorator(func):
        # wrapper
        def uvuci_wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            # uvlacenje
            return "%s%s" % (uvlacenje, res)

        return uvuci_wrapper

    return uvuci_decorator


@pozdrav_vreme_dekorisanje
def dobro_jutro_dekorisano(ime):
    return "Dobro jutro: %s" % ime


@pozdrav_vreme_dekorisanje
def dobar_dan_dekorisano(ime):
    return "Dobar dan: %s" % ime


@pozdrav_vreme_dekorisanje
def dobro_vece_dekorisano(ime):
    return "Dobro vece: %s" % ime


def dekoratori():
    # dekorisanje se radi prilikom prevodjenja
    print(">>> Upotreba dekoratora uz oslonac na Python interpreter.")
    print(dobro_jutro_dekorisano("Mika"))
    time.sleep(1)
    print(dobar_dan_dekorisano("Zika"))
    time.sleep(1)
    print(dobro_vece_dekorisano("Pera"))
    time.sleep(1)
    print(dobro_jutro_dekorisano("Mika"))
    time.sleep(1)
    print(dobar_dan_dekorisano("Zika"))
    time.sleep(1)
    print(dobro_vece_dekorisano("Pera"))
    # obratiti paznju na rezultate


@uvuci(broj_razmaka=4)
@pozdrav_vreme_dekorisanje
def dobro_jutro_stekovano(ime):
    return "Dobro jutro: %s" % ime


@uvuci(broj_razmaka=8)
@pozdrav_vreme_dekorisanje
def dobar_dan_stekovano(ime):
    return "Dobar dan: %s" % ime


@uvuci(broj_razmaka=12)
@pozdrav_vreme_dekorisanje
def dobro_vece_stekovano(ime):
    return "Dobro vece: %s" % ime


def dekoratori_stekovano():
    # dekoratori mogu da se stekuju
    print(dobro_jutro_stekovano("Mika"))
    time.sleep(1)
    print(dobar_dan_stekovano("Zika"))
    time.sleep(1)
    print(dobro_vece_stekovano("Pera"))
    time.sleep(1)
    print(dobro_jutro_stekovano("Mika"))
    time.sleep(1)
    print(dobar_dan_stekovano("Zika"))
    time.sleep(1)
    print(dobro_vece_stekovano("Pera"))


class A:
    @uvuci(broj_razmaka=20)
    @pozdrav_vreme_dekorisanje
    def pozdravi_a(self, ime, prezime):
        return "Pozdravljam: %s %s" % (ime, prezime)


def dekorator_metode():
    print(A().pozdravi_a("Mika", "Mikic"))


if __name__ == '__main__':
    # funkcije_kao_first_class_objekti()
    # dekoratori_rucno()
    # dekoratori()
    # dekoratori_stekovano()
    dekorator_metode()
