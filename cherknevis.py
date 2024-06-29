number = 1634
digits = [int(digit) for digit in str(number)]

for digit in digits:
    result = sum([digit**4 for digit in digits])
    if result == number:
        


