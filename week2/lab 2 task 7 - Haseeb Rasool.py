def main():
    # This program prints the first 20 numbers in the Fibonacci sequence
    a, b = 0, 1
    #variable a is initialized to 0 and variable b is initialized to 1. The Fibonacci sequence starts with these two numbers, and each subsequent number is the sum of the previous two numbers.
    for i in range(20):
        #for loop is used to iterate 20 times, which corresponds to the first 20 numbers in the Fibonacci sequence.
        print(a, end=" ")
        #print() function is used to print the current value of a, which represents the current number in the Fibonacci sequence. The end=" " argument is used to print the numbers on the same line with a space in between.
        a, b = b, a + b 
        #The line a, b = b, a + b updates the values of a and b for the next iteration. The new value of a becomes the previous value of b, and the new value of b becomes the sum of the previous values of a and b. This is how the Fibonacci sequence is generated.
    print()
        #The print() function is called again to move to the next line after printing all 20 numbers in the Fibonacci sequence.

if __name__ == "__main__":
    #The if __name__ == "__main__": statement checks if the script is being run directly (as opposed to being imported as a module). If it is being run directly, it calls the main() function to execute the program.
    main()
    