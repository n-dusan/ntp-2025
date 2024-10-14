# 4. Funkcije koje omogucavaju razne vrste iteracija

from itertools import chain, cycle, groupby, takewhile, dropwhile, tee


# 4.1 chain - vise iteratibilnih objekata posmatramo kao jedan
def chain_primer():
    niz1 = [2, 4, 6, 8, 10]
    niz2 = [1, 3, 5, 7, 9, 11]
    for i in chain(niz1, niz2):
        print(i)


# 4.2 cycle - moze biti korisno za iteracije po modulu
def cycle_primer():
    modulo_5 = [0, 1, 2, 3, 4]
    iteration_number = 10
    for i in cycle(modulo_5):
        print(i)
        iteration_number -= 1
        if iteration_number < 0:
            break


# 4.3 filter - vraca elemente koji zadovoljavaju odredjeni kriterijum
def filter_primer():
    # ugradjena funkcija filter
    niz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # filter je generator, pa ga raspakujemo u listu
    print(list(filter(lambda x: x % 2 == 0, niz)))


# 4.4. map - primena odredjene funkcije na sve elemenete iterabilnog objekta
# Moze biti zgodno paralelizovati.
def map_primer():
    niz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # povecavamo sve vrednosti
    print(list(map(lambda x: x + 1, niz)))


# 4.5. zip - paralelna iteracije kroz dve kolekcije
def zip_primer():
    niz1 = ["Mika", "Pera", "Zika"]
    niz2 = ["Mikic", "Peric", "Zikic"]
    for i, j in zip(niz1, niz2):
        print("%s %s" % (i, j))


# 4.6 groupby
def groupby_primer():
    string = "AAABBBBCCCCC"
    for k, g in groupby(string):
        print(k, len(list(g)))


# 4.7 takewhile - uzmi sve elemente s pocetka koji zadovoljavju uslov
def takewhile_primer():
    niz = range(100)
    print(list(takewhile(lambda x: x < 35, niz)))


# 4.8 dropwhile - odbaci sve elemente s pocetka koji zadovoljavaju uslov
def dropwhile_primer():
    niz = range(100)
    print(list(dropwhile(lambda x: x < 35, niz)))


# 4.9 tee - umnozava iterabilni objekat
def tee_primer():
    niz = range(20)
    for i in tee(niz, 5):
        # mozemo vise puta iterirati kroz isti iterabilni objekat
        print(list(i))


if __name__ == '__main__':
    chain_primer()
    cycle_primer()
    filter_primer()
    map_primer()
    zip_primer()
    groupby_primer()
    takewhile_primer()
    dropwhile_primer()
    tee_primer()
