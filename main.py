import random

class Kortti:
    def __init__(self):
        pass

class Pakka:
    def __init__(self):
        pass

class Poyta:
    def __init__(self):
        pass

class Logiikka:
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



# 1. logiikka yhdelle korttipinolle, vertailu (isompi vai pienempi)
# 2. laajennetaan yhdeksälle korttipinolle
# 3. mihin pinoista kortti laitetaan --> vertailu


class Logiikka:
    pino = []
    pino.append(Pakka.yksikortti(pakka))

    vertailu = input("isompi vai pienempi?")
    print ("Valinta:" + vertailu)



    while True:
        oikein = 0
        if vertailu == 'isompi':
            if Pakka.yksikortti(pakka) > poyta[pino-1][-1]:
                oikein += 1
                print("Oikein!")
                if oikein == 3:
                    print("Seuraavan pelaajan vuoro")
                    oikein = 0
                break
            else:
                print("Väärin! Juo " + str(len(poyta[pino-1])+1))
                break
        elif vertailu == 'pienempi':
            if Pakka.yksikortti(pakka) < poyta[pino-1][-1]:
                oikein += 1
                print("Oikein!")
                if oikein == 3:
                    print("Seuraavan pelaajan vuoro")
                    oikein = 0
                break
            else:
                print("Väärin! Juo " + str(len(poyta[pino-1])+1))
                break
