from art import logo, vs
from data import data
import random

print(logo)
print(vs)

account_a = random.choice(data)
account_b = random.choice(data)
if account_b == account_a:
    account_b = random.choice(data)

print(account_a)
print(account_b)
