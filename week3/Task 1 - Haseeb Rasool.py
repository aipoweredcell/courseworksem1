def password_analysis():
    #function to analyze the strength of a password entered by the user
    password=input("enter your password: ")
    #prompt the user to enter their password

    length = len(password)
    #calculate the length of the password
    uppercase=0
    #variable to count the number of uppercase letters in the password
    lowercase=0
    #variable to count the number of lowercase letters in the password
    numbers=0
    #variable to count the number of digits in the password
    symbols=0
    #variable to count the number of symbols in the password

    for char in password:
        #iterate through each character in the password and check if it is an uppercase letter, lowercase letter, digit, or symbol
        if char.isupper():
            #if the character is an uppercase letter, increment the uppercase counter by 1
            uppercase=uppercase+1
            #variable to count the number of uppercase letters in the password
        elif char.islower():
            #if the character is a lowercase letter, increment the lowercase counter by 1
            lowercase=lowercase+1
            #variable to count the number of lowercase letters in the password
        elif char.isdigit():
            #if the character is a digit, increment the numbers counter by 1
            numbers=numbers+1
            #variable to count the number of digits in the password
        else:
            #if the character is a symbol, increment the symbols counter by 1
            symbols=symbols+1 
            #variable to count the number of symbols in the password
            
    print("Password length:", length)
    #print the length of the password
    print("Uppercase letters:", uppercase)
    #print the number of uppercase letters in the password
    print("Lowercase letters:", lowercase)
    #print the number of lowercase letters in the password
    print("Numbers:", numbers)
    #print the number of digits in the password
    print("Symbols:", symbols)
    #print the number of symbols in the password

if __name__ == "__main__":
    #if the script is being run directly (not imported as a module), call the password_analysis function to start the password analysis process
    password_analysis() 
