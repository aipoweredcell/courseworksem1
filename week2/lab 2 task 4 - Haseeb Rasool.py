def main():
    #main function to execute the program
    while True:
        #prompt user for input and validate it is a whole number between 1-100
        try:
            #prompt user for input and validate it is a whole number between 1-100
            num = int(input("enter a number between 1-100"))
            #check if the number is between 1-100 and if it is even or odd
            if num < 1 or num > 100:
                #if the number is not between 1-100, print an error message and prompt user again
                print("error: number must be between 1-100")
                #pass the error message to the user and prompt for input again
            elif num % 2 == 0:
                #if the number is even, print a success message and break the loop
                print(f"success {num} is even")
                #break the loop
                break
            #if the number is odd, print a success message and break the loop
            else:
                #if the number is odd, print a success message and break the loop
                print(f"success: {num} is odd")
                #break the loop
                break  
            

        except ValueError:
            #exception handling for invalid input, print an error message and prompt user again
            print("Invalid input. please enter a whole number")
            #print an error message and prompt user again

if __name__ == "__main__":
    #execute the main function when the script is run directly
    main()
            