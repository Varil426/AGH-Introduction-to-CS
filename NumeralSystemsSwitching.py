def testNumber(number, inputSystem):
    if (number[0] == '-'):
        return 0
    for i in range(0, len(number)):
        codeValue = ord(number[i])
        if (inputSystem <= 10):
            if (codeValue < 48 or codeValue >= (48 + inputSystem)):
                return 1
        if (inputSystem > 10):
            if (codeValue >= 48 and codeValue <= 57):
                continue
            elif ((codeValue >= 65 or codeValue >= 97) and (codeValue < (65 + inputSystem - 10) or codeValue < (97 + inputSystem - 10))):
                continue
            else:
                return 1
    return 0

def toDecimal(number, inputSystem):
    result = 0
    for i in range(len(number) - 1, -1, -1):
        codeValue = ord(number[i])
        if (codeValue >= 48 and codeValue <= 57):
            codeValue -= 48
        elif (codeValue >= 65 and codeValue <= 90):
            codeValue -= 55
        elif (codeValue >= 97 and codeValue <= 122):
            codeValue -= 87
        result += codeValue * (inputSystem ** (len(number) - i - 1))
    return result

def fromDecimal(number, outputSystem):
    result = []
    while (int(number / outputSystem) != 0):
        temp = number % outputSystem
        number = int(number / outputSystem)
        if (temp < 10):
            result.append(chr(temp + 48))
        else:
            result.append(chr(temp + 54))
    temp = number % outputSystem
    if (temp < 10):
        result.append(chr(temp + 48))
    else:
        result.append(chr(temp + 54))
    result.reverse()
    return ''.join(result)

inputSystem = int(input("Input System (Give decimal number) = "))
number = input("Your number (Cannot be negative) = ")
outputSystem = int(input("Output System (Give decimal number) = "))
if (inputSystem <= 1 or outputSystem <= 1 or inputSystem > 36 or outputSystem > 36):
    print("Wrong number system")
else:
    if (testNumber(number, inputSystem)):
        print("Wrong Number")
    else:
        print(fromDecimal(toDecimal(number, inputSystem), outputSystem))