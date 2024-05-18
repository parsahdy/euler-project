from decimal import *
getcontext().prec = 1000


def recurring_cycle():
    d = 1000
    max_cycle_length = 0
    i_for_cycle = False
    for i in range(1, d):
        current_cycle = find_cycle_length(i)
        if current_cycle > max_cycle_length:
            max_cycle_length = current_cycle
            i_for_cycle = i

    print(i_for_cycle)

def find_cycle_length(n):
    cycle_length = 0
    reminders = []
    x = 1
    while True:
        if x % n == 0: 
            break
        elif x in reminders:
            break
        reminders.append(x)
        x = x*10 % n
        
        cycle_length += 1
        
    return cycle_length
            
recurring_cycle() 





