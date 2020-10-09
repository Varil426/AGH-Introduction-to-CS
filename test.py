tab  = []

for i in range (2,10):
    d=0
    for j in range (2, i-1):
        if (i%j==0):
            d=1
            break
        else:
            continue
    if(d == 0):
        tab.append(i)
print(tab)

def funkcja(h,dzien,noc,polka):
    obecna_pozycja = 0
    status = 0
    while obecna_pozycja < h:
        obecna_pozycja += dzien
        if obecna_pozycja < h :
            i = 1
            while i*polka <= obecna_pozycja:
                i+=1
            i -= 1
            if i*polka >= obecna_pozycja - noc and i*polka <= obecna_pozycja:
                obecna_pozycja = polka*i
            else:
                obecna_pozycja -= noc
        status += 1
        print(obecna_pozycja)
    return status

funkcja(21,5,1,3)