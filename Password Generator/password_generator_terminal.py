# Password Generator

import random

MIN_CHARS = 8
MAX_CHARS = 16

# create a list of each type of character in a typical password, along with a union of the whole group.
lc_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uc_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
all_chars = uc_letters + lc_letters + numbers + symbols

print("*** PASSWORD GENERATOR ***")

# limit the user's input, but give them a significant range for password length.
nr_chars = int(input(f"How many characters would you like in your password?({MIN_CHARS}-{MAX_CHARS})\n"))

# enforce that we are only allowing the 
while nr_chars < MIN_CHARS or nr_chars > MAX_CHARS:
    if nr_chars < MIN_CHARS:
        print(f"error: {nr_chars} is not enough characters for a secure password.")
    elif nr_chars > MAX_CHARS:
        print(f"error: {nr_chars} is too many characters for this password generator.")

    nr_chars = int(input("How many characters would you like in your password?(8-16)\n"))

#hold the password in a list temporarily to make the manipulation simple
password_list = []

#get 1 of each of our types of characters and add to the password
password_list.append(random.choice(lc_letters))
password_list.append(random.choice(uc_letters))
password_list.append(random.choice(numbers))
password_list.append(random.choice(symbols))

# add the rest of the password's characters randomly from all character options
for char in range(1, nr_chars + 1):
    password_list.append(random.choice(all_chars))

# randomize the characters in the list
random.shuffle(password_list)

# convert the list to a string and present it to the user.
password = ''
for char in password_list:
    password += char

print(f"Your password is: {password}")