from art import logo, vs
from data import data
import random

print(logo)
print(vs)

account_a = random.choice(data)
account_b = random.choice(data)
if account_b == account_a:
    account_b = random.choice(data)

account_name = account_a["name"]
account_descr = account_a["description"]
account_country = account_a["country"]
print(f'{account_name}, a {account_descr}, from {account_country}')
