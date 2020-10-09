length = int(input("Give me length: "))
while (length < 1):
    length = int(input("Give me LONGER length: "))
numberOfSpaces = length
numberOfX = 1
xInPartMAX = 3
now = 0
while (xInPartMAX <= (length*2 + 1)):
    while (numberOfX <= xInPartMAX):
        while (now < numberOfSpaces):
            print(" ", end = "")
            now += 1
        now = 0
        while (now < numberOfX):
            print("x", end = "")
            now += 1
        now = 0
        numberOfSpaces -= 1
        numberOfX += 2
        print()
    numberOfSpaces = length
    numberOfX = 1
    xInPartMAX += 2