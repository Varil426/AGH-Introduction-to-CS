def Cezar(napis, przesuniecie):
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

napis = "abc def"

print(Cezar(napis, 3))