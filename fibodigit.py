
x1 = 1
x2 = 1

fibo = []
while x1 < 10 ** 1000:
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    
    fibo.append(str(x1))

for num in fibo:
    if len(num) == 1000:
        print(num)
        print(fibo.index(num))

