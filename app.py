from CircleExample import *
from Circle import Circle

if __name__ == '__main__':
    ce = CircleExample(15.5)  # muutujale näitame ära diameetri
    # objekt.muutuja (self.diameter)
    print(ce.diameter)  # muutuja objektist
    # objekt.meetod() (def)
    ce.radius()  # väljasta raadius
    ce.area()  # väljasta pindala tekst
    print()  # tühi rida

    ce = CircleExample('Läheb katki')
    print(ce.diameter)
    # ce.radius()  # siin läheb katki
    ce.area()

    # võrdluseks kaks objekti
    ce1 = CircleExample(5)
    ce2 = CircleExample(5.5)
    if ce2.diameter > ce1.diameter:
        print('Teine on suurem')

    print()

    c = Circle(10)  # 10 on raadius (vaata klassis __init__)
    print(c.get_radius())  # see väljastab 10 antud hetkel
    print(c.get_diameter())  # see väljastab 20 antud hetkel
    print(2 * c.get_radius())  # see väljastab 20 antud hetkel
    print(c.get_perimeter())  # 62.83185307179586
    print(c.get_area())  # 314.1592653589793
    print(c.__str__())  # see on pikk tekst

    print()

    c1 = Circle(radius=5.4)
    print(c1.__str__())

    print()

    c2 = Circle(-6)
    if c2.get_radius() > 0:
        print('Lammas:', c2.__str__())
        print(f'Oinas: {c2.__str__()}')
        print('Siga:' + c2.__str__())