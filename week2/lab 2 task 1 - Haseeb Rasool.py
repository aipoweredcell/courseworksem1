def get_values():
    #gets 2 values from the user and returns them as floats
    value1 =float(input("Please enter the first value: "))
    value2 =float(input("Please enter the second value: "))
    return value1, value2

def display_results(value1, value2):
    #calculate and display the results of the calculations
    print("Sum: ", value1 + value2)
    #calculates the sum by adding the two values together and displays the result
    print("Product: ", value1 * value2)
    #calculates the product by multiplying the two values together and displays the result
    print("second value subtracted from first value: ", value1 - value2)
    #calculates the difference by subtracting the second value from the first value and displays the result

    if value2 != 0:
        #checks if the second value is not zero to avoid division by zero error
        print("Division: ", value1 / value2)
        #calculates the division by dividing the first value by the second value and displays the result
        print("Integer division: ", value1 // value2)
        #calculates the integer division by dividing the first value by the second value and displays the result
        print("Modulus: ", value1 % value2)
        #calculates the modulus by finding the remainder of the division of the first value by the second value and displays the result
    else:
        #displays a message if the second value is zero
        print("Division, integer division, and modulus are not possible when the second value is    zero.")
            #displays a warning message indicating that division, integer division, and modulus operations cannot be performed when the second value is zero.
    print("First value raised by the power of the second value: ", value1 ** value2)
    #calculates the first value raised to the power of the second value and displays the result

def main():
    #runs the program
    value1, value2 = get_values()
    #calls the get_values function to get two values from the user and assigns them to value1 and value2
    display_results(value1, value2)
    #calls the display_results function to perform calculations and display the results using the values obtained from the user


if __name__ == "__main__":
    main()
    