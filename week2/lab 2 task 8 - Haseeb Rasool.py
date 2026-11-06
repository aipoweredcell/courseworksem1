def event_counter():
    #function to count the number of incorrect password attempts
    incorrect=0
    #variable incorrect is initialized to 0. This variable will be used to keep track of the number of incorrect password attempts made by the user.

    for i in range(10):
        #for loop is used to iterate 10 times, which corresponds to the maximum number of password attempts allowed.
        pw=input("Password: ")
        #The input() function is used to prompt the user to enter a password. The entered password is stored in the variable pw.
        if pw != "secret":
            #If the entered password is not equal to the string "secret", it means the password attempt
            incorrect=incorrect+1
            #The variable incorrect is incremented by 1 to keep track of the number of incorrect password attempts made by the user.

    print("total incorrect", incorrect)
    #The print() function is used to display the total number of incorrect password attempts made by the user after all 10 attempts have been completed.
    if incorrect > 5:
        #If the total number of incorrect password attempts is greater than 5, it means that the user has made more than 50% incorrect attempts.
        print("ALERT: over 50% incorrect")
        #The print() function is used to display an alert message indicating that the user has made more than 50% incorrect password attempts. This serves as a warning to the user about their performance in entering the correct password.

def brute_force():
    #function to simulate a brute-force password guessing attempt
    attempts=0
    #variable attempts is initialized to 0. This variable will be used to keep track of the number of password guessing attempts made by the user.

    while attempts <3:
        #The while loop is used to allow the user to make password guessing attempts until the maximum number of attempts (3) is reached. The loop will continue as long as the value of attempts is less than 3.
        guess=input("passworfd guess: ")
        #The input() function is used to prompt the user to enter a password guess. The entered guess is stored in the variable guess.
        attempts=attempts+1
        #The variable attempts is incremented by 1 to keep track of the number of password guessing attempts made by the user. This ensures that the loop will eventually terminate after 3 attempts.

        if guess=="secret":
            #If the entered password guess is equal to the string "secret",
            print("success!")
            #The print() function is used to display a success message indicating that the user has correctly guessed the password. This serves as feedback to the user that their guess was correct.
            return
        #If the entered password guess is not equal to the string "secret

    print("Max amount of attempts reached")
    #The print() function is used to display a message indicating that the maximum number of password guessing attempts has been reached. This serves as feedback to the user that they have exhausted their allowed attempts and can no longer make further guesses.

def login():
    #function to simulate a login process with a maximum of 3 attempts
    
    failed=0
    #variable failed is initialized to 0. This variable will be used to keep track of the number of failed login attempts made by the user.

    while failed <3:
        #The while loop is used to allow the user to make login attempts until the maximum number of failed attempts (3) is reached. The loop will continue as long as the value of failed is less than 3.
        user=input("username: ")
        #The input() function is used to prompt the user to enter a username. The entered username is stored in the variable user.
        pw=input("password: ")
        #The input() function is used to prompt the user to enter a password. The entered password is stored in the variable pw.
        if user=="admin" and pw =="secret":
            #If the entered username is equal to the string "admin" and the entered password is equal to the string "secret", it means that
            print("success!")
            #The print() function is used to display a success message indicating that the user has successfully logged in. This serves as feedback to the user that their login credentials were correct.
            return
        #If the entered username and password do not match the expected values, it means that the login attempt has failed.
        else:
            #The else statement is executed when the login attempt fails. It indicates that the entered username and password do not match the expected values.
            failed=failed+1
            #The variable failed is incremented by 1 to keep track of the number of failed login attempts made by the user. This ensures that the loop will eventually terminate after 3 failed attempts.

    print("account is forzen for 24 hours")
    #The print() function is used to display a message indicating that the account is frozen for 24 hours. This serves as feedback to the user that they have exceeded the maximum number of allowed login attempts and will not be able to access the account for a specified period of time.

def main():
    #function to simulate a security tool with multiple options for the user to choose from
    while True:
            #The while loop is used to create an infinite loop that will continue until the user chooses to exit the program. This allows the user to repeatedly access the different options available in the security tool.
            user=input("startup user: ")
            #The input() function is used to prompt the user to enter a username for the startup login process. The entered username is stored in the variable user.
            pw=input("startup pass: ")
            #The input() function is used to prompt the user to enter a password for the startup login process. The entered password is stored in the variable pw.
            if user=="admin" and pw=="secret":
                #If the entered username is equal to the string "admin" and the entered password is equal to the string "secret", it means that the startup
                print("startup login successful!\n")
                #The print() function is used to display a success message indicating that the startup login was successful. This serves as feedback to the user that their login credentials were correct and they can proceed to access the security tool.
                break
            #If the entered username and password do not match the expected values, it means that the startup login attempt has failed.

    while True:
        #The while loop is used to create an infinite loop that will continue until the user chooses to exit the program. This allows the user to repeatedly access the different options available in the security tool.
        choice=input("\n1. counter\n2. brute-force\n3. login\n4. exit\nchoice: ")
        #The input() function is used to prompt the user to enter their choice from the available options in the security tool. The entered choice is stored in the variable choice.

        if choice =="1":
            #The if statement checks if the user's choice is equal to the string "1", which corresponds to the option for the event counter functionality in the security tool.
            event_counter()
            #The event_counter() function is called to execute the event counter functionality. This function will count the number of incorrect password attempts made by the user and provide feedback accordingly.
        elif choice =="2":
            #The elif statement checks if the user's choice is equal to the string "2", which corresponds to the option for the brute-force password guessing functionality in the security tool.
            brute_force()
            #The brute_force() function is called to execute the brute-force password guessing functionality. This function will allow the user to make password guessing attempts and provide feedback on their success or failure.
        elif choice =="3":
            #The elif statement checks if the user's choice is equal to the string "3", which corresponds to the option for the login functionality in the security tool.
            login()
            #The login() function is called to execute the login functionality. This function will allow the user to attempt to log in with a username and password, providing feedback on their success or failure.
        elif choice=="4":
            #The elif statement checks if the user's choice is equal to the string "4", which corresponds to the option to exit the security tool.
            print("thank you for using the security tool")
            #The print() function is used to display a thank you message to the user for using the security tool. This serves as a polite farewell message before exiting the program.
            break
        #The break statement is used to exit the while loop, effectively terminating the program and ending the execution of the security tool.
        else:
            #The else statement is executed when the user's choice does not match any of the available options in the security tool. It indicates that the entered choice is invalid.
            print("Invalid choice. try again")
            #The print() function is used to display an error message indicating that the user's choice is invalid. This serves as feedback to the user, prompting them to enter a valid option from the available choices in the security tool.

if __name__ == "__main__":
    #The if __name__ == "__main__": statement checks if the script is being run directly (as opposed to being imported as a module). If it is being run directly, it calls the main() function to execute the program.
    main()

