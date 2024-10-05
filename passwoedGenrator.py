import random
import string

def generate_password(length, include_special_chars):
    first_char = random.choice(string.ascii_letters)
    
    if include_special_chars:
        all_chars = string.ascii_letters + string.digits + string.punctuation
    else:
        all_chars = string.ascii_letters + string.digits
    
    remaining_chars = ''.join(random.choice(all_chars) for _ in range(length - 1))
    
    password = first_char + remaining_chars
    return password

password_length = int(input("Enter the desired password length: "))
include_special_chars = input("Do you want to include special characters (y/n)? ").lower() == 'y'
print(generate_password(password_length, include_special_chars))
