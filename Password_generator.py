import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
try:

    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    if nr_symbols <= 0 or nr_numbers <= 0 or nr_letters <= 0:
        raise ValueError("enter a positve number! and bigger than 0")
except ValueError as e:
    print(f"Error: {e}")
    exit()

digit = ""

for number in range(0, nr_letters):
    digit += random.choice(letters)
for number in range(0, nr_symbols):
    digit += random.choice(symbols)
for number in range(0, nr_numbers):
    digit += random.choice(numbers)

digit_list = list(digit)

random.shuffle(digit_list)

digit = ""
for char in digit_list:
    digit += char
    
print(f"Your password is: {digit}")
