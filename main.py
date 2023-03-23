# Password Generator 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n──────────» Welcome to the Password Generator «──────────\n")

nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input(f"How many symbols would you like in your password?: "))
nr_numbers = int(input(f"How many numbers would you like in your password?: "))

random_string = ''.join(random.choices(letters, k = nr_letters))
random_symbols = ''.join(random.choices(symbols, k = nr_symbols))
random_numbers = ''.join(random.choices(numbers, k = nr_numbers))

password_sum = random_string + random_symbols + str(random_numbers)

password_list = []

for i in password_sum:
  password_list.append(i)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print("\n     ======================================")
print(f"         Your password is: {password}")
print("     ======================================\n")
