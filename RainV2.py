import random
import time
import os

random.seed()

height = int(input("Height = "))
width = int(input("Width = "))
status = []

for i in range(0, height):
    status.append(-1)
while(1):
    status[0] = random.randrange(width)
    for k in status:
        if k != -1:
            print(" " * k + "x")
    time.sleep(0.3)
    os.system('cls')
    for k in range(height - 1, 0, -1):
        status[k] = status[k - 1]