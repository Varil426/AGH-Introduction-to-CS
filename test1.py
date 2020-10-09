def kolo(x, y, r):
    while (x-r < 1 or x+r>21):
        r -= 1
    while (y-r < 1 or y+r>21):
        r -= 1
    margin = 0.5
    for i in range(1,21):
        for j in range(1, 21):
            if ((j-x)**2+(i-y)**2 <= (r+margin)*(r+margin)):
                print('x', end='')
            else:
                print('.', end='')
        print()
        
kolo(9, 9, 5)