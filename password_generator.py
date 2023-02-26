import os
import random
import re
import string
import sys

import pyperclip


def generate_password(min_length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    chars = letters
    if numbers:
        chars += digits
    if special_chars:
        chars += special

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(chars)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special

    return password


pwd_min_length = int(input("Enter the length of your password: "))
pwd_has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
pwd_has_special = input("Do you want to have special chars (y/n)? ").lower() == "y"
pwd = generate_password(pwd_min_length, pwd_has_number, pwd_has_special)
pyperclip.copy(pwd)
print("The generated password is and copied to your clipboard:", pwd)
