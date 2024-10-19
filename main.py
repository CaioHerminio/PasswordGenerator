import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("WELCOME TO THE PASSWORD GENERATOR!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like in your password?\n"))

# Version 1

#password = ""

#for char in range(1, n_letters + 1):
  #password = password + random.choice(letters)

#for char in range(1, n_numbers + 1):
  #password = password + random.choice(numbers)

#for char in range(1, n_symbols + 1):
  #password = password + random.choice(symbols)

#print(password)


# Version 2

password = []

for char in range(1, n_letters + 1):
  password.append(random.choice(letters))

for char in range(1, n_numbers + 1):
  password.append(random.choice(numbers))

for char in range(1, n_symbols + 1):
  password.append(random.choice(symbols))

random.shuffle(password)

new_password = ""
for char in password:
  new_password = new_password + char  

print(f"Your new password is {new_password}. Keep it safe, and don't show it to anyone!")
