def main():
    # This program prompts the user to enter a password and checks if it matches the correct password.
    while True:
        # Prompt the user to enter a password
        password = input("Enter password: ")
        # Check if the entered password matches the correct password

        if password == "secret":
            #if the password is correct, print "Access granted!" and break the loop
            print("Access granted!")
            #print("Access granted!")
            break
        #break the loop if the password is correct
        else:
            #if the password is incorrect, print "Incorrect password. try again" and continue the loop
            print("Incorrect password. try again")
            #prints "Incorrect password. try again" if the password is incorrect

if __name__ == "__main__":
    # Call the main function to start the program
    main()