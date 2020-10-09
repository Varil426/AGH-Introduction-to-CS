import random

T = []
def fill(tab):
    for i in range (0, 4):
        tab.append(random.randrange(1, 101))

def wybieranie(tab):
    for i in range(0, len(tab)):
        m = i
        for j in range(i, len(tab)):
            if (tab[j] < tab[m]):
                m = j
        tmp = tab[i]
        tab[i] = tab[m]
        tab[m] = tmp
        
def wstawianie(tab):
    for i in range (1, len(tab)):
        for j in range(i - 1, -1, -1):
            if(tab[i] < tab[j]):
                tab.insert(j, tab.pop(i))
                break
            if (j == 0 and tab[i] <= tab[j]):
                tab.insert(0, tab.pop(i))
                break

def buble(tab):
    i = 0
    j = 1
    while(j):
        print(j)
        if(tab[i] > tab[i + 1]):
            tab[i], tab[i + 1] = tab[i + 1], tab[i]
            j += 1
        if(i == (len(tab) - 1)):
            if (j == 1):
                j = 0
            elif (j != 1):
                j = 1
            i = 0
        

fill(T)
T1 = T.copy()
T2 = T.copy()
T3 = T.copy()
print(T)
wybieranie(T1)
print(T1)
wstawianie(T2)
print(T2)
buble(T3)
print(T3)