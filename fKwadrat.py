import matplotlib.pyplot as plt
import math

a1 = float(input("a1 = "))
b1 = float(input("b1 = "))
c1 = float(input("c1 = "))

a2 = float(input("a2 = "))
b2 = float(input("b2 = "))
c2 = float(input("c2 = "))

def rys(a,b,c,start,end):
    k = []
    l = []
    for x in range(int(start - start / 2),int(end + end / 2)):
        y = a * x ** 2 + b * x + c
        k.append(x)
        l.append(y)
    axes.plot(k,l)

def licz(a1,b1,c1,a2,b2,c2):
    a = a1 - a2
    b = b1 - b2
    c = c1 - c2
    if (a == 0 and b == 0 and c == 0):
        return "Nieskonczenie wiele punktow wspolnych"
    if (a == 0):
        if (b != 0):
            return [(-c) / b]
        else:
            if (c == 0):
                return "Nieskonczenie wiele punktow wspolnych"
            else:
                return "Brak punktow wspolnych"
    delta = (b * b) - (4 * a * c)
    if delta == 0:
        return (-b / (2 * a))
    elif delta < 0:
        return "Brak punktow wspolnych"
    else:
        return [((-b + math.sqrt(delta)) / (2 * a)), ((-b - math.sqrt(delta)) / (2 * a))]
    

fig = plt.figure()
axes = fig.add_subplot(111)

a = licz(a1,b1,c1,a2,b2,c2)
if (len(a) == 1):
    print("Jeden punkt wspolny: (" + str(a[0]) + ", " + str(a1 * a[0] ** 2 + b1 * a[0] + c1) + ")")
    rys(a1,b1,c1,a[0] - 10,a[0] + 10)
    rys(a2,b2,c2,a[0] - 10,a[0] + 10)
if (len(a) == 2):
    print("Dwa punkty wspolne: (" + str(a[0]) + ", " + str(a1 * a[0] ** 2 + b1 * a[0] + c1) + ") (" + str(a[1]) + ", " + str(a1 * a[1] ** 2 + b1 * a[1] + c1) + ")")
    if (a[0] >= a[1]):
        max = a[0]
        min = a[1]
    else:
        max = a[1]
        min = a[0]
    rys(a1,b1,c1,min - 10,max + 10)
    rys(a2,b2,c2,min - 10,max + 10)
else:
    print(a)
    rys(a1,b1,c1,-100,100)
    rys(a2,b2,c2,-100,100)

plt.show()