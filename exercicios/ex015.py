''' EX015 - CAR RENTAL
Create a program that asks the total of km driven by a rented car and total of days rented. Calculate the price to pay knowing the car rental costs $60 per day and $0.15 per km driven.

INITIAL DATA
> Read number of days rented (variable)
> Read total of km driven (variable)

Calculate price to pay:
(0.15 * km_driven) + (60 * days_rented) (variable)
'''

from colorama import Fore, Style

print("-=" * 15)
print("CAR RENTAL".center(30))
print("-=" * 15)
print()

km_driven = int(input("How many kilometers did you drive during rental? "))
days_rented = int(input("How many days did you rent the car? "))
price = (0.15 * km_driven) + (60 * days_rented)

print(f"\nPrice to pay: {Fore.YELLOW}${price:.2f}{Style.RESET_ALL}")
