digit_fifth_powers = []
for number in range(2, 1000000):
    digits = [int(digit) for digit in str(number)]
    result = sum([digit**5 for digit in digits])
    if result == number:
        digit_fifth_powers.append(number)
        
        
print(sum(digit_fifth_powers))
