import random
import string
def low_level(n,c):
    char_l=""
    for i in range(1,n+1):
        char_l+=random.choice(string.ascii_letters)
    return char_l

def medium_level(n,c):
    char_m=""
    for i in range(1,n+1):
        char_m+=random.choice(string.ascii_letters+string.digits)
    return char_m

def high_level(n,c):
    char_h=""
    special_characters=['@','#','$','&','*','_','-','!']
    special_string="".join(str(elem) for elem in special_characters)
    for i in range(1,n+1):
        char_h+=random.choice(string.ascii_letters+string.digits+special_string)
    return char_h

def password(n,c):
    if (c==1):
        password = low_level(n,c)
        print("Password  : ",password)
    elif(c==2):
        password = medium_level(n,c)
        print("Password  : ",password)
    elif(c==3):
        password = high_level(n,c)
        print("Password  : ",password)
    else:
        print("Invalid Choice!")


print("Welcome To Password Generator!")
length=int(input("Please enter length of password you want : \n"))
complexity=int(input("Please choose the Complexity level : \n1:Low\n2:Medium\n3:High\n"))
password(length,complexity)