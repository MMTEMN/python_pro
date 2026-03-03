import random
import time

def gen_pass(pass_length):
    elements = "+-/*!&$#514988?=@<>abcdefghijklmnopqrstwyzx"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

print(gen_pass(10))

def yazi_tura():
    para=random.randint(0,2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA" 
    
def saatsoyle():
    s = time.strftime ( "%H:%M:%S" )
    return s  ## 24 saat formatı ## time.strftime ( " %H:%M:%S" ) ## 12 saat formatı ## time.strftime ( "%I:%M: % S " )
