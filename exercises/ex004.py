''' EX004 - Basic Value Analysis
Create a program that reads a value from user and prints its type and all info possible about it
'''

user_input = input("Type anything: ")

print()
print(f"Value type: {type(user_input)}")

print(f"Is it space only? {user_input.isspace()}")
print(f"Is it numeric? {user_input.isnumeric()}")
print(f"Is it alphabetic? {user_input.isalpha()}")
print(f"Is it alphanumeric? {user_input.isalnum()}")
print(f"Is it all uppercase? {user_input.isupper()}")
print(f"Is it all lowercase? {user_input.islower()}")
print(f"Is it capitalized? {user_input.istitle()}")
print(f"Is it a valid identifier? {user_input.isidentifier()}")
print(f"Is it ASCII? {user_input.isascii()}")
print(f"Is it decimal? {user_input.isdecimal()}")
print(f"Is it digit? {user_input.isdigit()}")
