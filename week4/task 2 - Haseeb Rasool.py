def authenticate(username, password):
    #defines the function that accepts username and password
    if username=="admin" and password == "admin123":
        #checks if supplied username and password are correct
        return True
    return False

def main():
    print("--- System Login ---")

    while True:
        try:
            username = input("Enter username: ")
            #asks for user input
            password = input("enter password: ")


            if authenticate(username, password):
                #calls authenticate function to verify cred
                print("login successful")
                break
            else:
                print("invalid username or password try again.\n")

        except Exception as e:
            #catches unexpected exceptions during input or execution 
            print(f"An error occured: {e}. please try again.\n") 


if __name__=="__main__":
    main()