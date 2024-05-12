def code_is_ok(code_digits):
    if code_digits['five']+code_digits['three'] == 14 and \
          code_digits['one'] == 2*code_digits['two']-1 and \
            code_digits['four'] == code_digits['two']+1 and \
                code_digits['two']+code_digits['three'] == 10 and \
                    code_digits['one']+code_digits['two']+code_digits['three']+code_digits['four']+code_digits['five'] == 30:
        return True



for code in range(0, 100000):
    code_str = str(code).zfill(5)
    
    code_digits = {}
    code_digits['one'] = int(code_str[0])
    code_digits['two'] = int(code_str[1])
    code_digits['three'] = int(code_str[2])
    code_digits['four'] = int(code_str[3])
    code_digits['five'] = int(code_str[4])

    if code_is_ok(code_digits):
        print(code)



#version2

def code_is_ok(code_digits):
    if int(code_digits[4])+int(code_digits[2]) == 14 and \
          int(code_digits[0]) == 2*int(code_digits[1])-1 and \
            int(code_digits[3]) == int(code_digits[1])+1 and \
                int(code_digits[1])+int(code_digits[2]) == 10 and \
                    int(code_digits[0])+int(code_digits[1])+int(code_digits[2])+int(code_digits[3])+int(code_digits[4]) == 30:
        return True



for code in range(0, 100000):
    code_digits = str(code).zfill(5)
    
    if code_is_ok(code_digits):
        print(code)



    

 
    
        


