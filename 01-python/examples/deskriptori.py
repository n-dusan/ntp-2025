# 3. Deskriptori

# 3.1 problem sa properties


class PrirodanBrojProperties:
    def __init__(self, broj):
        self._prirodan_broj = 1

    @property
    def prirodan_broj(self):
        return self._prirodan_broj

    @prirodan_broj.setter
    def prirodan_broj(self, broj):
        if not isinstance(broj, int):
            raise ValueError("Broj mora biti ceo")
        if broj <= 0:
            raise ValueError("Broj nije prirodan")
        self._prirodan_broj = broj


class PrirodanBroj():
    def __set_name__(self, owner, name):
        # Instancira se u vreme kreiranja owner klase.
        # Name je naziv atributa na nivou te klase.
        # Owner je klasa u kojoj se atribut nalazi.
        self.name = name

    def __get__(self, instance, owner):
        # Poziva se prilikom iscitavanja vrednosti atributa.
        # instance: instanca klase koja sadrzi atributa
        # owner: klasa koja sadrzi atributa
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # Poziva se prilikom pisanja vrednosti atributa.
        if not isinstance(value, int):
            raise ValueError("Broj mora biti tipa int")
        if value <= 0:
            raise ValueError("Broj mora biti veci od nule")
        instance.__dict__[self.name] = value


class Par:
    # manipulacija objektom (u ovom slucaju dobijanje vrednosit i postavljanje vrednosti atributa)
    # se prosledjuje klasi PrirodanBroj

    prvi = PrirodanBroj()  # kreira se instance klase PrirodaBroj(Par, "prvi")
    drugi = PrirodanBroj()  # kreira se instance klase PrirodaBroj(Par, "drugi")

    def __init__(self, prvi, drugi):
        self.prvi = prvi
        self.drugi = drugi

    def __str__(self):
        return "(%d, %d)" % (self.prvi, self.drugi)

    # nema boiler plate koda u nasoj klasi
    # mozemo na vise mesta da odradimo istu proveru


def test_properties():
    print(">>> Prirodan broj upotrebom koncepta Properties")
    # Test PrirodanBrojProperties
    pbp = PrirodanBrojProperties(100)
    pbp.prirodan_broj = 1
    print(pbp.prirodan_broj)
    pbp.prirodan_broj = 3
    print(pbp.prirodan_broj)
    try:
        pbp.prirodan_broj = -1
    except ValueError:
        print("Broj nije prirodan")


def test_descriptors():
    print(">>> Prirodan broj upotrebom koncepta Descriptor")
    # Test PrirodanBrojDescriptor
    p1 = Par(1, 2)
    p2 = Par(3, 4)
    print("%s, %s" % (p1, p2))
    p1.prvi = 5
    p1.drugi = 6
    p2.prvi = 7
    p2.drugi = 8
    print(p1, p2)
    try:
        p1.prvi = 1.0
    except:
        print("Broj nije prirodan")


if __name__ == '__main__':
    test_properties()
    test_descriptors()
