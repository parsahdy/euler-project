n = 12

prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False

if prime:
    print('It is prime')
else:
    print('Not prime')

