import random

choises = ['1','2','3','4','5','6','7','8','9','0''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z''`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',',','<','.','>','/','?']

n = int(input("enter the length of the password : "))

password = ""
for i in range(n):
    choice = random.choice(choises)
    password += choice

print(password)

good = input("is the password "+ password +" good (y/n) : ")

if good == 'n' or good == 'N':
    print("too bad")