import random
import string

def validate_password(password):
    #validates if pass meets min length of 8 chars and has variety of no. symbols etc
    if len(password) < 8:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.islower():
            has_lower=True
        elif char.isupper():
            has_upper= True
        elif char.isdigit():
            has_digit=True
        elif char in string.punctuation:
            has_symbol= True
    #If requirements met, = True


    has_letter = has_lower or has_upper
    return has_letter and has_digit and has_symbol


def validate_ip(ip_str):
    #checks Ip format: must have 4 octects separated by dots, each between 0 and 255
    parts=ip_str.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if len(part) > 1 and part[0] == '0':
            return False
    return True
def generate_strong_password():
    #generates a random stron password 
    length= random.randint(10,16)
    lower=random.choice(string.ascii_lowercase)
    upper=random.choice(string.ascii_uppercase)
    digit=random.choice(string.digits)
    symbol=random.choice(string.punctuation)

    all_chars=string.ascii_letters + string.digits + string.punctuation
    remaining_length=length -4

    password_chars=[lower, upper, digit, symbol]
    for _ in range(remaining_length):
        password_chars.append(random.choice(all_chars))

    random.shuffle(password_chars)
    return "".join(password_chars)