from art import logo, vs
from data import data
import random


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f'{account_name}, a {account_descr}, from {account_country}'


print(logo)
print(vs)

account_a = random.choice(data)
account_b = random.choice(data)
if account_b == account_a:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(f"Compare A: {format_data(account_b)}.")
