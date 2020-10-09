D = [0,1,2,3,4,5,6,7,8,9,10]
C = [0,1,5,8,9,10,16,17,20,24,26]
Z = []
S = []

#Program może nie działać, gdyby długości nie były co 1, bo nie odwołuje się nigdzie do tych długości, tylko pętle idą co 1, możliwa poprawa modyfikując for'y

def max(n):
    max = 0
    for i in range(1, len(n)):
        if(n[i] > n[max]):
            max = i
    return max

def zysk(l):
    if (l < len(Z)):
        return (Z[l])
    elif (l == 0):
        return 0
    else:
        potential = []
        for i in range(0, l):
            if i == 0:
                potential.append(C[l])
            else:
                potential.append(zysk(i) + zysk(l - i))
        x = max(potential)
        Z.append(potential[x])
        if x != 0:
            S[l].append(x)
        return potential[x]

def SModify():
    for i in range(0, len(S)):
        if S[i]:
            j = S[i][0]
            tmp = []
            for k in range(0, len(S[j])):
                tmp.append(S[j][k])
            S[i] = tmp + S[i]
            tmp.clear()
            for k in range(0, len(S[i - j])):
                tmp.append(S[i - j][k] + j)
            S[i] += tmp

for i in range(0, len(D)):
    S.append([])
zysk(len(D) - 1)
SModify()
for i in range(0, len(D)):
    print("Dla preta o dlugosci " + str(D[i]) + " max = " + str(Z[i]) + " Ciecia po " + str(S[i]) + " metrach")