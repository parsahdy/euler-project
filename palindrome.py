def palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
    

max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if palindrome(i * j):
            if i * j > max:
                max = i * j
                
print(max)