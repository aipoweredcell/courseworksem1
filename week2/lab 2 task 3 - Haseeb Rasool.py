def read_egg_count():
    #gets user input for number of eggs and validates it is a whole number
    """read and validate a whole number of eggs"""
    while True:
        #prompt user for input and validate it is a whole number
        try:
            #prompt user for input and validate it is a whole number
            eggs_text = input("Enter the number of eggs: ")
            #convert input to integer and check if it is non-negative
            eggs = int(eggs_text)
            #check if the number of eggs is non-negative
            if eggs >= 0:
            #if the number of eggs is non-negative, return the value
                return eggs
            #if the number of eggs is negative, print an error message
        except ValueError:
            #exception handling for invalid input, print an error message and prompt user again
            pass
        #pass the error message to the user and prompt for input again
            print("Invalid input. please enter a valid whole number")
            #displays text asking teh user for input again

def calc_egg_breakdown(total_eggs):
    #function to calculate the breakdown of total eggs into gross, dozen, and single eggs
    """break down total eggs into gross, dozen and single using integer division"""
    #calculate the number of gross eggs, dozen eggs, and single eggs using integer division and modulus
    gross = total_eggs // 144
    #calculate the remainder after calculating gross eggs
    remainder_after_gross = total_eggs % 144
    #calculate the number of dozen eggs and single eggs using integer division and modulus

    dozen = remainder_after_gross // 12
    #calculate the remainder after calculating dozen eggs
    single = remainder_after_gross % 12
    #return the calculated values of gross, dozen, and single eggs
    return gross, dozen, single
    #returns the calculated values of gross, dozen, and single eggs to the calling function

def main():
    #main function to execute the program
    total_eggs = read_egg_count()
    #calculate the breakdown of total eggs into gross, dozen, and single eggs
    gross, dozen, single = calc_egg_breakdown(total_eggs)
    #display the output of the breakdown of total eggs into gross, dozen, and single eggs

    print(f"Output {total_eggs} eggs is {gross} gross eggs + dozen eggs is {dozen} + {single} eggs")
    #display the output of the breakdown of total eggs into gross, dozen, and single eggs 

if __name__ == "__main__":
    #execute the main function when the script is run directly
    main()   