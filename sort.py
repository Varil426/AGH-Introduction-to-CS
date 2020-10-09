import random

def wybieranie(tab):
    for i in range(0, len(tab)):
        minimum = i
        for j in range(i, len(tab)):
            if (tab[j] < tab[minimum]):
                minimum = j
        tmp = tab[i]
        tab[i] = tab[minimum]
        tab[minimum] = tmp
            
def minimum(tab):
    minimum = tab[0]
    for i in range(0, len(tab)):
        if (tab[i] < minimum):
            minimum = tab[i]
    print(minimum)

def fill(tab, size):
    for i in range(0, size):
        tab.append(random.randrange(1, 101))

def partition(tab, s, f):
        counter = s
        for i in range(s+1, f+1):
                if (tab[counter] > tab[i]):
                        tab.insert(counter, tab.pop(i))
                        counter += 1
        return counter

def quickSort(tab, s, f):
        if (s < f):
                p = partition(tab, s, f)
                quickSort(tab, s, p-1)
                quickSort(tab, p+1, f)

#def merge(tab1, tab2):
#        i = 0
#        j = 0
#        T = []
#        for a in range(0, len(tab1) + len(tab2)):
#                if (tab1[i] < tab2[j]):
#                        T.append(tab1[i])
#                        i += 1
#                else:
#                        T.append(tab2[j])
#                        j += 1
#                if (i == len(tab1)-1):
#                        for z in range(j, len(tab2)):
#                                T.append(tab2[z])
#                        break
#                if (j == len(tab2)-1):
#                        for z in range(i, len(tab1)):
#                                T.append(tab1[z])
#                        break
#        return T
#
#def mergeSort(tab, s, f):
#        if (s < f):
#                return merge(mergeSort(tab, s, int(f/2)), mergeSort(tab, int(f/2+1), f))
#        T = []
#        T.append(tab[s])
#        return T

T = []
fill(T, 5)
T1 = T.copy()
T2 = T.copy()
print(T)
wybieranie(T)
print(T)
minimum(T)
print(T1)
quickSort(T1, 0, len(T1)-1)
print(T1)
#print(T2)
#print(mergeSort(T2, 0, len(T2)-1))