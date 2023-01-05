import random

kortti = 0
pakka = []
poyta = []

print(kortti)


def teePakka():
    a = 1
    for m in ["Pata", "Risti", "Ruutu", "Hertta"]:
        for i in range(1, 14):
            pakka.append(m, a)

teePakka()
print(pakka)


def sekoitaPakka(pakka: list):
    random.shuffle(pakka)
    return pakka




def pelaus():
    pino = []
    pino.append(Pakka.yksikortti(pakka))

    vertailu = str(input("isompi (+) vai pienempi (-)?"))
    print("Valinta:" + vertailu)

    while True:
        oikein = 0
        if vertailu == '+':
            if Pakka.yksikortti(pakka) > poyta[pino - 1]:
                oikein += 1
                print("Oikein!")
                if oikein == 3:
                    print("Seuraavan pelaajan vuoro")
                    oikein = 0
                break
            else:
                print("Väärin! Juo " + str(len(poyta[pino - 1]) + 1))
                break
        elif vertailu == '-':
            if Pakka.yksikortti(pakka) < poyta[pino - 1][-1]:
                oikein += 1
                print("Oikein!")
                if oikein == 3:
                    print("Seuraavan pelaajan vuoro")
                    oikein = 0
                break
            else:
                print("Väärin! Juo " + str(len(poyta[pino - 1]) + 1))
                break


pelaus()
