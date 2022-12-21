import random

class Kortti:
    def __init__(self):
        pass

class Pakka:
    def __init__(self):
        pass

class Pelaaja:
    def __init__(self):
        pass

class Poyta:
    def __init__(self):
        pass

class Kortti:
    def __init__(self, maa, arvo):
        self.maa = maa
        self.value = arvo

    def show(self):         
        print ("{} {}".format(self.maa, self.value))


class Pakka:
    def __init__(self):
        self.kortit = []
        self.kokoa()

    def kokoa(self):
        for m in ["Pata", "Risti", "Ruutu", "Hertta"]:
            for a in range(1, 14):
                self.kortit.append(Kortti(m, a))

    def show(self):
        for c in self.kortit:
            c.show()

    def sekoitaPakka(self):
        for i in range(len(self.kortit) -1, 0, -1):
            r = random.randint(0, i)
            self.kortit[i], self.kortit[r] = self.kortit[r], self.kortit[i]

    def yksikortti(self):
        nostetut = []
        nostetut.insert(1, self.kortit.pop())
        return nostetut


class Poyta(Pakka):
    def __init__(self):
        self.pelit = []
        oikein = 0


    def luoPoyta(self):
        poyta = [[] for _ in range(9)]
        for i in range(9):
            jako = pakka.yksikortti()
            poyta[i].append(jako)
            pakka.kortit.pop(0)
            print(i + 1)
        a = (' ___' *  3 )
        b = '   '.join('||||')
        print('\n'.join((a, b, a, b, a, b, a, )))

pakka = Pakka()
pakka.sekoitaPakka()
# pakka.show()
poyta = Poyta()
poyta.luoPoyta()