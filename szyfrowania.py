def Cezar(napis, przesuniecie):
    napis = napis.lower()
    napis = list(napis)
    for i in range(0, len(napis)):
        if (ord(napis[i]) == ord(' ')):
            continue
        elif (ord(napis[i])+przesuniecie>122):
            k=ord(napis[i]) + przesuniecie - 122
            new = 97 + k
            napis[i] = chr(new)
        else:
            napis[i] = chr(ord(napis[i]) + przesuniecie)
    return "".join(napis)

def Brutus(kod, przesuniecie):
    kod = kod.lower()
    kod = list(kod)
    for i in range(0, len(napis)):
        if (ord(kod[i]) == ord(' ')):
            continue
        elif (ord(kod[i])-przesuniecie<97):
            k=ord(kod[i]) - przesuniecie + 26
            kod[i] = chr(k)
        else:
            kod[i] = chr(ord(kod[i]) - przesuniecie)
    return "".join(kod)

def Podstawieniowy(napis, alfabet):
    napis = napis.lower()
    alfabet = list(alfabet)
    napis = list(napis)
    for i in range(0, len(napis)):
        if (ord(napis[i]) == ord(' ')):
            continue
        else:
            numerWAlfabecie = ord(napis[i]) - 97
            napis[i] = alfabet[numerWAlfabecie]
    return "".join(napis)

def dePodstawieniowy(napis, alfabet):
    napis = napis.lower()
    alfabet = alfabet.lower()
    alfabet = list(alfabet)
    napis = list(napis)
    for i in range(0, len(napis)):
        if (ord(napis[i]) == ord(' ')):
            continue
        else:
            index = alfabet.index(napis[i])
            napis[i] = chr(97 + index)
    return "".join(napis)

def zKluczem(napis, klucz):
    napis = napis.lower()
    klucz = klucz.lower()
    klucz = list(klucz)
    napis = list(napis)
    literaWKluczu = 0
    for i in range(0, len(napis)):
        litera = ord(napis[i])
        if (litera == ord(' ')):
            continue
        przesuniecie = ord(klucz[literaWKluczu]) - 96
        if (litera + przesuniecie > 122):
            napis[i] = chr(litera + przesuniecie - 26)
        else:
            napis[i] = chr(litera + przesuniecie)
        literaWKluczu += 1
        if (literaWKluczu >= len(klucz)):
            literaWKluczu = 0
    return "".join(napis)

def deZKluczem(napis, klucz):
    napis = napis.lower()
    klucz = klucz.lower()
    klucz = list(klucz)
    napis = list(napis)
    literaWKluczu = 0
    for i in range(0, len(napis)):
        litera = ord(napis[i])
        if (litera == ord(' ')):
            continue
        przesuniecie = ord(klucz[literaWKluczu]) - 96
        if (litera - przesuniecie < 97):
            napis[i] = chr(litera - przesuniecie + 26)
        else:
            napis[i] = chr(litera - przesuniecie)
        literaWKluczu += 1
        if (literaWKluczu >= len(klucz)):
            literaWKluczu = 0
    return "".join(napis)

napis = "abc def"
zaszyfrowaneCezarem = Cezar(napis, 3)
zaszyfrowanePodstawieniowo = Podstawieniowy(napis, "qwertyuiopasdfghjklzxcvbnm")
zaszyfrowaneZKluczem = zKluczem(napis, "abc")

print("\nCezar:")
print(zaszyfrowaneCezarem)
print(Brutus(zaszyfrowaneCezarem,3))
print("\nPodstawieniowo:")
print(zaszyfrowanePodstawieniowo)
print(dePodstawieniowy(zaszyfrowanePodstawieniowo, "qwertyuiopasdfghjklzxcvbnm"))
print("\nZ Kluczem:")
print(zaszyfrowaneZKluczem)
print(deZKluczem(zaszyfrowaneZKluczem, "abc"))