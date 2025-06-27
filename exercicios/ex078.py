''' EX078 - Biggest and Smallest in a List
Create a program that reads 5 numbers from user and store it in a list. In the end, print the biggest and smallest number read and its positions in the list.
'''

number_list = []

for c in range(0, 5):
    user_input = int(input(f"Type a number for position {c}: "))

    number_list.append(user_input)


max_value = max(number_list)
min_value = min(number_list)

# Lists for the indexes
max_value_i = []
min_value_i = []

# Verify several index occurrences
for i, v in enumerate(number_list):
    if v == max_value:
        max_value_i.append(i)

    if v == min_value:
        min_value_i.append(i)


print(f"\nThe biggest number in the list is {max_value} in the positions {max_value_i}.")
print(f"The smallest number in the list is {min_value} in the positions {min_value_i}.")

