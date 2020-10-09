import os
import time

height = 2
width = 2
while (height % 2 != 1 or width % 2 != 1):
    height = int(input("Height = "))
    width = int(input("Width = "))
center = [int(height/2), int(width/2)]
if (center[0] <= center[1]):
    MAX = center[0]
else:
    MAX = center[1]
growing = True
state = 0
while(1):
    for i in range(0, height):
        for j in range(0, width):
            if (((i + state) == center[0]) or ((i - state) == center[0])):
                if (j <= center[1]):
                    if ((j + state) >= center[1]):
                        print("*", end="")
                    else:
                        print(" ", end="")
                elif (j > center[1]):
                    if ((j - state) <= center[1]):
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
            elif (i <= center[0]):
                if ((i + state) >= center[0]):
                    if (((j + state) == center[1]) or ((j - state) == center[1])):
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
            elif (i > center[0]):
                if ((i - state) <= center[0]):
                    if (((j + state) == center[1]) or ((j - state) == center[1])):
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
            else:
                print(" ", end="")
        print()
    if (state == MAX):
        growing = False
    if (state == 0):
        growing = True
    if (growing):
        state += 1
    else:
        state -= 1
    time.sleep(0.3)
    os.system("cls")
