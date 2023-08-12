#!/usr/bin/python3
def validate_password(password):
    if len(password)
    return False
has_upper = False
has_lower = False
has_digit = False
for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if char.isspace():
        has_digit = False
return has_upper and has_lower and has_digit