# primeri sa slajdova 52-62 (http://www.igordejanovic.net/courses/ntp/python_napredni.html#52)

from collections import OrderedDict


# Mocna je stvar, ali zna da se zakomplikuje
# Stoga treba voditi racuna kada se koristi visestruko nasledjivanje
# Kako se u Javi realizuje visestruko nasledjivanje?

class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        super().__setitem__(key, value)


class LoggingOD(LoggingDict, OrderedDict):
    pass


def primer1():
    print(LoggingOD.__mro__)


# Sta kada imamo razlicit potpis funkcije
# Bitno je sve iscrpeti sve **kwargs
class Root:
    def draw(self):
        # nema dalje propagacije uz MRO lanac
        # mi smo implementirati koren
        assert not hasattr(super(), 'draw')


class Shape(Root):
    def __init__(self, shapename, **kwargs):
        self.shapename = shapename
        super().__init__(**kwargs)

    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()


class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        super().__init__(**kwargs)

    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()


def primer2():
    cs = ColoredShape(color='red', shapename='circle')
    cs.draw()
    print(cs.__class__.__mro__)


"""
object
    Root
        Shape
            ColoredShape
"""


# upotreba adaptera
class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print('Drawing at position:', self.x, self.y)


class MoveableAdapter(Root):
    def __init__(self, x, y, **kwds):
        self.movable = Moveable(x, y)
        super().__init__(**kwds)

    def draw(self):
        self.movable.draw()
        super().draw()


class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass


def primer3():
    mcs = MovableColoredShape(color='red', shapename='triangle', x=10, y=20)
    mcs.draw()
    # obratiti paznju na MRO lanac
    print(mcs.__class__.__mro__)


"""
object
    Root
        Shape
            ColoredShape
                MovableColoredShape (ovo se pojavljuje pre u MRO lancu od MoveableAdapter)
        MoveableAdapter(sadrzi u sebi Moveable)
            MovableColoredShape    
            
"""

if __name__ == '__main__':
    primer1()
    primer2()
    primer3()
