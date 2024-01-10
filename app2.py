"""
Loome listi erinevate ringide jaoks, kus raadiused on vahemikus 1-10 ühikut ning ringe on listi tehtud 5tk.
Raadiused on juhuslikud
"""
from random import randint
from Circle import *

circles = []  # ringide list (algselt tühi)

if __name__ == '__main__':
    for x in range(5):
        circles.append(Circle(randint(1, 10)))
    print('Ringide arv listis: ', len(circles))

    #  Väljasta kõikide ringide info (raadius, diameeter, ümbermõõt..)
    for circle in circles:
        print(circle.__str__())
    print('-----')
    # Versioon 2
    for x in range(len(circles)):
        print(circles[x].__str__())
    print('Kõige suurema raadiusega:')

    # Väljastage listist kõige suurema raadiusega ringi info
    r = []  # Leitud raadiuste list
    for circle in circles:
        r.append(circle.get_radius())  # Lisa raadius listi
    index = r.index(max(r))  # Leia suurima raadiuse indeks listist
    print(circles[index].__str__())  # Väljasta õige raadiusega ring
