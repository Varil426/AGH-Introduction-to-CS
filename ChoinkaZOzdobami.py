n=int(input("Podaj liczbę większą lub równą 2: "))

#Pełna choinka
row = 1
for i in range(1,n+1):
    z = n
    for j in range(1, i+2):
        if (row)%2==1:
            if (j)==1:
                print("  "*z + "! ")
            else:
                print("  "*z + "! " + "* "*(2*(j-2)+1) + "! ")
        else:
            print("  " *z, end="")
            for k in range(0,(j-1)*2+1):
                if (k+3)%4==0:
                    print("o ", end="")
                else:
                    print("* ", end="")
            print()
        z -= 1
        row += 1

