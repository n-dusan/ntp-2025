# 3. Funkcije viseg reda
# Funkcije višeg reda su funkcije koje primaju funkcije kao parametre i/ili vraćaju funkcije.

from functools import partial, reduce, wraps, total_ordering
from operator import mul


# 3.1 partial - Parcijalna aplikacije funkcije

def saberi(a, b):
    return a + b


def partial_primer():
    # zamrzavamo drugi parametar
    increment = partial(saberi, b=1)
    # zamrzavamo prvi parametar
    decrement = partial(saberi, a=-1)
    print(increment(10))
    # moramo eksplicitno pozvati argument b
    print(decrement(b=10))


# 3.2 reduce - redukcija nad kolekcijom

# racunanje faktorijela upotrebom redukcije
def faktoriel(n):
    return reduce(mul, range(1, n + 1), 1)


def reduce_primer():
    for i in range(11):
        print("%d, %d" % (i, faktoriel(i)))


# 3.3 update_wrapper i wraps (ocuvamo naziv funkcije, dokumentaciju, ...)
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Poziv dekorisane funkcije')
        return f(*args, **kwds)

    return wrapper


@my_decorator
def funkcija_koja_se_dekorise():
    """Dokumentacija"""
    print('Poziv originalne funkcije')


def update_wrapper_primer():
    funkcija_koja_se_dekorise()
    print(funkcija_koja_se_dekorise.__name__)
    print(funkcija_koja_se_dekorise.__doc__)
    # TODO: pozivi ponovo ovu funkciju, ali ukloni @wraps(f)
    # Da nije iskoriscne @wrap, ime bi bilo wrapper, a Docstring """Dokumentacija""" bi se izgubio.


# 3.4 total_ordering
@total_ordering
class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def get_tupple(self):
        return self.ime.upper(), self.prezime.upper()

    def __eq__(self, other):
        return self.get_tupple() == other.get_tupple()

    def __lt__(self, other):
        return self.get_tupple() < other.get_tupple()


def total_ordering_primer():
    o1 = Osoba("Mika", "Mikic")
    o2 = Osoba("Pera", "Peric")
    o3 = Osoba("mika", "mikic")
    print(o1 == o2)
    print(o1 == o3)
    print(o1 < o2)
    print(o1 >= o2)
    print(o1 <= o2)


if __name__ == '__main__':
    partial_primer()
    reduce_primer()
    update_wrapper_primer()
    total_ordering_primer()
