def validate_password(password):
    #check if the password is under 10 cahrs
    if len(password) < 10 or ' ' in password:
        #checks if passwrd is too short
        return False
    #returns false immediately if lenght or space check fails 

    upper, lower, digits, symbols = 0,0,0,0
    for c in password:
        if c.isupper(): upper +=1
        elif c.islower(): lower +=1
        elif c.isdigit(): digits +=1
        elif c in "!@#$%": symbols +=1
    return upper >= 1 and lower >= 1 and digits >= 2 and symbols >= 1


def main():
    while True:
        username=input("Enter username: ")
        password=input("enter password: ")


        if validate_password(password):
            print(f"Success! '{username}' registered.\n")
            break
        print("Invalid password. try again.\n")

if __name__=="__main__":
    main()