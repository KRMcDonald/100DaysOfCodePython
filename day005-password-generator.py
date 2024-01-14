#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwordstr1 = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#letters
for xletter in range(0,nr_letters):
  yletter = random.randint(0,len(letters))
  passwordstr1 += letters[yletter-1]

#symbols
for xsymbol in range(0,nr_symbols):
  ysymbol = random.randint(0,len(symbols))
  passwordstr1 += symbols[ysymbol-1]

#numbers
for xnumber in range(0,nr_numbers):
  ynumber = random.randint(0,len(numbers))
  passwordstr1 += numbers[ynumber-1]

print("Easy solution: ")
print(passwordstr1)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passwordstr2 = ""

let_list = []
num_list = []
sym_list = []

#letters
for xletter in range(0,nr_letters):
  yletter = random.randint(0,len(letters))
  let_list += letters[yletter-1]

#symbols
for xsymbol in range(0,nr_symbols):
  ysymbol = random.randint(0,len(symbols))
  sym_list += symbols[ysymbol-1]

#numbers
for xnumber in range(0,nr_numbers):
  ynumber = random.randint(0,len(numbers))
  num_list += numbers[ynumber-1]

combined_list = let_list + sym_list + num_list
comb_len1 = len(combined_list)
comb_len2 = len(combined_list)

for l in range(0,comb_len1):
  z_index = random.randint(0,comb_len2 - 1)
  passwordstr2 += combined_list[z_index]
  del combined_list[z_index]
  comb_len2 = len(combined_list)

print("Hard solution: ")
print(passwordstr2)