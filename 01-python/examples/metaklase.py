# Klase su objekti, pa se njihove klase nazivaju metaklase
# class = sintaticki secer za poziv type metaklase


class A:
    pass


def primer1():
    # upotrebom type mozemo proveriti i kojoj klasi neki objekat pripada
    # koja je klasa klase A
    print(type(A))
    print(isinstance(A, type))
    # koja je klasa objekta a
    a = A()
    print(type(a))
    print(isinstance(a, A))
    # Sta je funkcija u Python-u?
    print(type(primer1))
    print(callable(primer1))


def primer2():
    print()
    # klasa moze da se kreira direktno upotrebom type metaklase
    B = type('B', (), {})
    print(type(B))
    b = B()
    print(type(b))


# definisemo metaklasu MojaMeta
class MojaMeta(type):
    pass


# definisemo klasu C cija je metaklasa MojaMeta
class C(metaclass=MojaMeta):
    pass


def primer3():
    print()
    print(type(C))
    c = C()
    print(type(c))


# vise informacija o metaklasama moze se pronaci na:
# 1. https://realpython.com/python-metaclasses/
# 2. https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/

if __name__ == '__main__':
    primer1()
    primer2()
    primer3()
