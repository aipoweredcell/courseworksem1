def main():
    #main function to execute the program
    while True:
        #prompt user for input and validate it is a whole number
        try:
            #prompt user for input and validate it is a whole number
            num = int(input("Enter a number"))
            #if the input is a valid whole number, print the multiplication table for that number
            for i in range(1, 11):
                #print the multiplication table for the input number
                print(f"{num} is x {i} = {num * i}")
                #if the input is a valid whole number, print the multiplication table for that number
            break
        #if the input is not a valid whole number, print an error message and prompt user again
        except ValueError:
            #exception handling for invalid input, print an error message and prompt user again
            print("Invalid input, please enter a valid number")
            #print an error message and prompt user again

if __name__ == "__main__":
    #execute the main function when the script is run directly
    main()