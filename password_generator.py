import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

a=random.randint(0,len(letters)-1)
lett=letters[a]
for i in range(0,nr_letters-1):
    a=random.randint(0,len(letters)-1)
    lett=lett+letters[a]
    
b=random.randint(0,len(symbols)-1)    
sym=symbols[b]

for i in range(0,nr_symbols-1):
    b=random.randint(0,len(symbols)-1)
    sym=sym+symbols[b] 
    
c=random.randint(0,len(numbers)-1)
numb=numbers[c]

for i in range(0,nr_numbers-1):
    c=random.randint(0,len(numbers)-1)
    numb=numb+numbers[c]


password=list(lett+sym+numb)
random.shuffle(password)

final_password=""
for i in password:
    final_password+=i
print(f"Your password is={final_password}")
