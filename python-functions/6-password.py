#!/usr/bin/python3
def validate_password(password):
    if len(password) < 8:
        return False
    
has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    elif char == ' ':
        return False
        
return has_upper and has_lower and has_digit
    