#!/usr/bin/python3
def validate_password(password):
    if len(password) < 8:
        return False
    
has_upper = False
has_lower = False
has_digit = False
has_space = False

for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if char.isspace():
        has_digit = True
        
        return has_upper and has_lower and has_digit and not has_space
    