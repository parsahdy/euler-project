import time
start_time = time.time()

def number_to_word(num):
    less_than_20 = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

    tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
            60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    thousands = {1_000: 'one thousand'}

        
    if num < 20:
        return less_than_20[num]
        
    elif num < 100:
        tens_digit = num // 10 * 10
        ones_digit = num % 10
        if ones_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit] + less_than_20[ones_digit]
        
    elif num < 1_000:
        hundreds_digit = num // 100
        remainder = num % 100
        if remainder == 0:
            return less_than_20[hundreds_digit] + 'hundred'
        else:
            return less_than_20[hundreds_digit] + 'hundredand' + number_to_word(remainder)
        
    elif num == 1_000:
        return thousands[1_000]

num_list = []
for n in range(1, 1001):
    num_list.append(number_to_word(n))


len_word = []
for word in num_list:
    word_without_spaces = word.replace(' ' , '').replace('-', '')
    len_word.append(len(word_without_spaces))

print(sum(len_word))
print("process finished --- %s seconds ---" % (time.time() - start_time))