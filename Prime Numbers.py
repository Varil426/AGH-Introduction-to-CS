import time

def primeNumbers(max):
    tab = []
    for i in range(2, max + 1):
        tab.append(i)
    for i in range(0, max - 1):
        value = tab[i]
        while(tab[i] != -1 and (value + tab[i]) <= max):
            tab[i + value] = -1
            value += tab[i]
    #for i in range (0, max - 1):
    #    if(tab[i] != -1):
    #       print(tab[i])

print("1. Auto")
print("2. Manual")
mode = input("Select mode (NUMBER): ")
if (mode == '1'):
    start = int(input("Select starting point: "))
    increase = int(input("Select how much to increase: "))
    if (start < 2):
        print("Invalid number, select more than 1")
    elif (increase < 0):
        print("Invalid number, select more than 0")
    else:
        for i in range (0, 20):
            start_time = time.time()
            primeNumbers(start + (i * increase))
            print("Test #" + str(i + 1) + " For: " + str(start + (i * increase)) +" Time: " + str(time.time() - start_time))
elif (mode == '2'):
    for i in range (0, 20):
        max = int(input("Test #" + str(i + 1) + " MAX = "))
        if(max < 2):
            print("Invalid number, test failed")
        else:
            start_time = time.time()
            primeNumbers(max)
            print(time.time() - start_time)
else:
    print("Invalid option")