def password_validator():
    #function to validate the password based on the specified policy requirements
    while True:
        #prompt the user to enter their password
        password = input("enter your password: ")
        #check the length of the password and initialize counters for different character types

        length = len(password)
        #initialize counters for uppercase letters, lowercase letters, digits, symbols, spaces, and invalid symbols
        uppercase_count = 0
        #variable to store the count of uppercase letters in the password
        lowercase_count = 0
        #variable to store the count of lowercase letters in the password
        digit_count = 0
        #variable to store the count of digits in the password
        symbol_count = 0
        #variable to store the count of symbols in the password
        has_space = False
        #variable to store whether the password contains any spaces
        invalid_symbol = False
        #variable to store whether the password contains any invalid symbols

        for char in password:
            #iterate through each character in the password and update the counters based on the character type
            if char.isupper():
                #increment the uppercase letter count if the character is an uppercase letter
                uppercase_count += 1
                #increment the uppercase letter count if the character is an uppercase letter
            elif char.islower():
                #increment the lowercase letter count if the character is a lowercase letter
                lowercase_count += 1
                #increment the lowercase letter count if the character is a lowercase letter
            elif char.isdigit():
                #increment the digit count if the character is a digit
                digit_count += 1
                #increment the digit count if the character is a digit
            elif char == ' ':
                #set the has_space flag to True if the character is a space
                has_space = True
                #set the has_space flag to True if the character is a space
            elif char in "!@#$%":
                #increment the symbol count if the character is a valid symbol
                symbol_count += 1
                #increment the symbol count if the character is a valid symbol
            else:
                #set the invalid_symbol flag to True if the character is an invalid symbol
                invalid_symbol = True
                #set the invalid_symbol flag to True if the character is an invalid symbol

        if (length >= 10 and
            #check if the password meets all the policy requirements and print an appropriate message
                uppercase_count >= 1 and
                #check if the password meets all the policy requirements and print an appropriate message
                lowercase_count >= 1 and
                #check if the password meets all the policy requirements and print an appropriate message
                digit_count >= 2 and
                #check if the password meets all the policy requirements and print an appropriate message
                symbol_count >= 1 and
                #check if the password meets all the policy requirements and print an appropriate message
                not has_space and
                #check if the password meets all the policy requirements and print an appropriate message
                not invalid_symbol):
                #check if the password meets all the policy requirements and print an appropriate message
            print("Password accepted! it meets all policy requirements")
            #print a message indicating that the password meets all policy requirements
            break
        #if the password does not meet all the policy requirements, print an appropriate message
        else:
            #if the password does not meet all the policy requirements, print an appropriate message
            print("Invalid password! please make sure that all policy requirements are met")
            #print a message indicating that the password does not meet all policy requirements


if __name__ == "__main__":
    #if the script is being run directly (not imported as a module), call the password_validator function to start the password validation process
    password_validator()