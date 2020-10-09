import random

def fill(tab, n):
    for i in range(0, n):
        tab.append(random.randrange(1,101))

def Partition(tab, s, f):
    i = s
    for j in range(s + 1, f):
        if (tab[j] <= tab[i]):
            tab.insert(i, tab.pop(j))
            i += 1
    return i

def QuickSort(tab, s, f):
    if (s < f):
        p = Partition(tab, s, f)
        print(str(tab) + str(tab[p]))
        QuickSort(tab, s, p-1)
        QuickSort(tab, p+1, f)

T = []
fill(T, 10)
print(T)
#print(Partition(T, 0, 10))
QuickSort(T, 0, 10)
print(T)