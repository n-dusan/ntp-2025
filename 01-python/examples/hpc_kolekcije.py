# 5. Kolekcije

from collections import OrderedDict, namedtuple, Counter, defaultdict, deque
from time import time
from functools import wraps


# 5.1 OrderedDict
# cuva redosled dodavanja elemenata
# move_to_end - prebacuje kljuc na kraj
def ordered_dict_primer():
    od = OrderedDict()
    for i in range(10):
        od[str(i)] = i

    for k, v in od.items():
        print(k, v)

    # prebaci na kraj
    od.move_to_end('3', last=True)
    print("===" * 11)
    for k, v in od.items():
        print(k, v)


# 5.1 Namedtuple - imenovana torka
def namedtuple_primer():
    # podseca malo na strukture u C-u
    Tacka = namedtuple('Tacka', ['x', 'y'])
    t = Tacka(x=3, y=5)
    print(t[0], t[1])
    print(t.x, t.y)
    X, Y = t
    print(X, Y)
    print(t)


# 5.2 Counter - recnik koji moze pomoci u prebrojavanju objekata
# objekti moraju da se hesiraju
def counter_primer():
    lista = [1, 2, 3, '1', '2', '3', 1, 2, 3, '1', '2', '3', 1, 2, 3]
    prebroj_elemente_list = Counter(lista)
    print(prebroj_elemente_list)
    print(prebroj_elemente_list.most_common(3))


# 5.3 defaultdict - mozemo da specificiramo podrazumevanu vrednost ako se pristupi nepostojecem kljucu
def defaultdict_primer():
    # moze biti zgodno ako rucno radimo neka prebrojavanja
    dd = defaultdict(int)
    for i in range(10):
        dd['A'] = dd['A'] + 1
    print(dd['A'])


# 5.4 deque
# ako nam trebaju dobre perfromanse, trebalo bi razmotriti upotrebu deka
def vreme(f):
    @wraps(f)
    def meri_vreme(*args, **kwargs):
        bt = time()
        f(*args, *kwargs)
        et = time()
        print("Funkcija: %s traje: %s" % (f.__name__, et - bt))

    return meri_vreme


def deque_primer():
    broj_elemenata = int(10e7)
    lista = list(range(broj_elemenata))
    dek = deque(range(broj_elemenata))

    @vreme
    def list_add_last():
        lista.append(3)

    @vreme
    def list_add_first():
        lista.insert(0, 3)

    @vreme
    def list_pop_last():
        lista.pop(-1)

    @vreme
    def list_pop_first():
        lista.pop(0)

    list_add_last()
    list_add_first()
    list_pop_last()
    list_pop_first()
    print("===" * 11)

    @vreme
    def deque_add_last():
        dek.append(3)

    @vreme
    def deque_add_first():
        dek.appendleft(3)

    @vreme
    def deque_pop_last():
        dek.pop()

    @vreme
    def deque_pop_first():
        dek.popleft()

    deque_add_last()
    deque_add_first()
    deque_pop_last()
    deque_pop_first()


if __name__ == '__main__':
    ordered_dict_primer()
    namedtuple_primer()
    counter_primer()
    defaultdict_primer()
    deque_primer()
