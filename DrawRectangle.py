height =  int(input("Height = "))
width = int(input("Width = "))

# Metoda 1

for i in range (0, height):
    print("*" * width)
print()

# Metoda 2

for i in range (0, height):
    for j in range(0, width):
        print("*", end = "")
    print()

