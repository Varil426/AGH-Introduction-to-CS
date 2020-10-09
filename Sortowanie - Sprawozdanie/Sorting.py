import random
import time

numberOfSort = 8
randRange = 10001
numberOfElements = 10
numberOfTests = 10
step = 1000
displayResults = 1

def fill(tab, size):
    for i in range(0, size):
        tab.append(random.randrange(1, randRange))

def selectionSort(tab):
    for i in range(0, len(tab)):
        minimum = i
        for j in range(i, len(tab)):
            if (tab[j] < tab[minimum]):
                minimum = j
        tmp = tab[i]
        tab[i] = tab[minimum]
        tab[minimum] = tmp

def insertionSort(tab):
    for i in range(1, len(tab)):
            if (tab[i] < tab[i - 1]):
                    for j in range(i - 1, -1, -1):
                            if (tab[j] < tab[i]):
                                    tab.insert(j+1, tab.pop(i))
                                    break
                            elif (j == 0):
                                    tab.insert(j, tab.pop(i))

def bubbleSort(tab):
    for i in range(0, len(tab)):
            for j in range(0, len(tab) - i - 1):
                    if (tab[j] > tab[j + 1]):
                            tab[j], tab[j+1] = tab[j+1], tab[j]

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

def mergeSort(tab): 
    if (len(tab) > 1): 
        middle = len(tab)//2
        L = tab[:middle] 
        R = tab[middle:]
        mergeSort(L) 
        mergeSort(R)
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                tab[k] = L[i] 
                i+=1
            else: 
                tab[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            tab[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            tab[k] = R[j] 
            j+=1
            k+=1

def makeHeap(tab, n, i): 
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and tab[i] < tab[l]: 
                largest = l 
        if r < n and tab[largest] < tab[r]: 
                largest = r 
        if largest != i: 
                tab[i],tab[largest] = tab[largest],tab[i]
                makeHeap(tab, n, largest) 

def heapSort(tab):
        length = len(tab)
        for i in range(length, -1, -1): 
                makeHeap(tab, length, i) 
        for i in range(length-1, 0, -1): 
                tab[i], tab[0] = tab[0], tab[i]
                makeHeap(tab, i, 0)

def bucketSort(tab, min, max):
        buckets = []
        numberOfBuckets = int(len(tab)/2)
        if (numberOfBuckets == 0):
                numberOfBuckets = 1
        delta = ((max - min)/numberOfBuckets)
        for i in range(0, numberOfBuckets):
                buckets.append([])
        for i in range(0, len(tab)):
                buckets[int((tab[i] - min)/delta)].append(tab[i])
        tab.clear()
        for i in range(0, numberOfBuckets):
                bubbleSort(buckets[i])
                tab += buckets[i]

def radixCompare(tab, position):
    n = len(tab) 
    output = [0] * (n) 
    count = [0] * (10) 
    for i in range(0, n): 
        index = (tab[i]/position) 
        count[ int((index)%10) ] += 1
    for i in range(1,10): 
        count[i] += count[i-1] 
    i = n-1
    while i>=0: 
        index = (tab[i]/position) 
        output[ count[ int((index)%10) ] - 1] = tab[i] 
        count[ int((index)%10) ] -= 1
        i -= 1
    i = 0
    for i in range(0,len(tab)): 
        tab[i] = output[i] 

def radixSort(tab): 
    maximum = max(tab) 
    position = 1
    while maximum/position > 0: 
        radixCompare(tab,position) 
        position *= 10
        
######################################
numberOfElements = int(input("Choose number of elements in array at the beginning: "))
while (numberOfElements < 1):
        numberOfElements = int(input("You must choose not less than 1\nChose number of elements in array at the beginning: "))
numberOfTests = int(input("Choose number of tests: "))
while (numberOfTests < 1):
        numberOfTests = int(input("You must choose not less than 1\nChose number of tests: "))
step = int(input("Choose step: "))
while (step < 0):
        step = int(input("You must choose not less than 0\nChoose step: "))
displayResults = int(input("Display results?\n1.Yes\n2.No\n"))
while (displayResults != 1 and displayResults != 2):
        displayResults = int(input("Select number\nDisplay results?\n1.Yes\n2.No\n"))
results = []
for i in range(0, numberOfSort):
        results.append([])
testingStart = time.time()
for i in range(0, numberOfTests):
        T = []
        fill(T, numberOfElements + i * step)
        Tabs = []
        for i in range(0, numberOfSort):
                Tabs.append(T.copy())

        sortStart = time.time()
        bubbleSort(Tabs[0])
        results[0].append(time.time() - sortStart) 

        sortStart = time.time()
        insertionSort(Tabs[1])
        results[1].append(time.time() - sortStart) 

        sortStart = time.time()
        selectionSort(Tabs[2])
        results[2].append(time.time() - sortStart) 
        
        sortStart = time.time()
        quickSort(Tabs[3],0,len(Tabs[3]) - 1)
        results[3].append(time.time() - sortStart) 
        
        sortStart = time.time()
        mergeSort(Tabs[4])
        results[4].append(time.time() - sortStart) 
        
        sortStart = time.time()
        heapSort(Tabs[5])
        results[5].append(time.time() - sortStart) 
        
        sortStart = time.time()
        bucketSort(Tabs[6], 0, randRange)
        results[6].append(time.time() - sortStart) 

        sortStart = time.time()
        radixSort(Tabs[7])
        results[7].append(time.time() - sortStart)

        if (displayResults == 1):
                print("\nTest number #" + str(i))
                print("Original Tab")
                print(T)
                print("Sorted Tabs")
                for i in range(0, numberOfSort):
                        print(Tabs[i])
                print()

print("Time for all tests: " + str(time.time() - testingStart))

f = open("bubbleSort.txt","w+")
for i in range(0, len(results[0])):
        f.write(str(results[0][i]) + "\t" + str(numberOfElements + i * step) + "\n")
f.close()

f = open("insertionSort.txt","w+")
for i in range(0, len(results[1])):
        f.write(str(results[1][i]) + "\t" + str(numberOfElements + i * step) + "\n")
f.close()

f = open("selectionSort.txt","w+")
for i in range(0, len(results[2])):
        f.write(str(results[2][i]) + "\t" + str(numberOfElements + i * step) + "\n")
f.close()

f = open("quickSort.txt","w+")
for i in range(0, len(results[3])):
        f.write(str(results[3][i]) + "\t" + str(numberOfElements + i * step) + "\n")
f.close()

f = open("mergeSort.txt","w+")
for i in range(0, len(results[4])):
        f.write(str(results[4][i]) + "\t" + str(numberOfElements + i * step) + "\n")
f.close()

f = open("heapSort.txt","w+")
for i in range(0, len(results[5])):
        f.write(str(results[5][i]) + "\t" + str(numberOfElements + i * step) + "\n")
f.close()

f = open("bucketSort.txt","w+")
for i in range(0, len(results[6])):
        f.write(str(results[6][i]) + "\t" + str(numberOfElements + i * step) + "\n")
f.close()

f = open("radixtSort.txt","w+")
for i in range(0, len(results[7])):
        f.write(str(results[7][i]) + "\t" + str(numberOfElements + i * step) + "\n")
f.close()
######################################
