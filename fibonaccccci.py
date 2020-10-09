T=[0,1]

def Fib(n):
    if (n<len(T)):
        x=T[n]
    else:
        x=Fib(n-1)+Fib(n-2)
        T.append(x)
    return x


print(Fib(4))