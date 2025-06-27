''' EX027 - First and Last Name
Create program that reads a person's full name, and prints out their first and last name separately.
'''

name = input("Enter your name: ")

print("Pleasure to meet you!")
print(f"Your first name is {name.split()[0]}") # Separate substrs in a list and takes the first index
print(f"Your last name is {name.split()[-1]}") # Separate substrs in a list and takes the last index
