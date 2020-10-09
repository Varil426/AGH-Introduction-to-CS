length = int(input("Give me length: "))
while (length < 2):
    length = int(input("Give me LONGER length: "))
currentPartMAX = 2
currentRowMAX = 1
now = 0
while (currentPartMAX <= length):
    while (currentRowMAX <= currentPartMAX):
        while (now < currentRowMAX):
            print("x", end = "")
            now += 1
        print()
        now = 0
        currentRowMAX += 1
    currentPartMAX += 1
    currentRowMAX = 1