import random
#importing the required libraries
from datetime import datetime
#import datetime library to get the current date and time
import socket
#importing the socket library to get the IP address of the user

def security_event_logger():
    #define the correct username and password
    correct_username="admin"
    #define the correct password
    correct_password="Password123!"
    #variable to store the success status of the login attempt

    print("SECURITY EVENT LOG")
    #print the security event log header
    print("==================")

    while True:
        #start an infinite loop to continuously prompt the user for login credentials
        username=input("enter your username please: ")
        #prompt the user to enter their username
        password=input("please enter your password: ")
        #prompt the user to enter their password

        event_id=random.randint(1000, 9999)
        #generate a random event ID between 1000 and 9999
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #get the current date and time and format it as a string
        try:
            #create a socket object to get the IP address of the user
            s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #connect to a public DNS server to determine the local IP address
            s.connect(("8.8.8.8", 80))
            #get the local IP address of the user
            ip_address=s.getsockname()[0]
            #close the socket connection
            s.close()
            #if there is an exception while getting the IP address, set it to a default value
        except Exception:
            #set the IP address to a default value if there is an exception
            ip_address="127.0.0.1"
            #variable to store the success status of the login attempt

        if username==correct_username and password==correct_password:
            #if the entered username and password match the correct credentials, set the event status to "successful login" and the success status to True
            event_status="successful login"
            #set the success status to True
            is_success=True
            #variable to store the success status of the login attempt
        else:
            #if the entered username and password do not match the correct credentials, set the event status to "failed login" and the success status to False
            event_status="failed login"
            #set the success status to False
            is_success=False
            #variable to store the success status of the login attempt

        print(f"Event ID: {event_id}")
        #print the event ID
        print(f"Username: {username}")
        #print the entered username
        print(f"Event Status: {event_status}")
        #print the event status (successful or failed login)
        print(f"IP Address: {ip_address}")
        #print the IP address of the user
        print(f"Timestamp: {timestamp}\n")
        #print the timestamp of the login attempt

        if is_success:
            #if the login attempt was successful, print a message indicating that access has been granted and break out of the loop to end the program
            print("access granted. session started.")
            #print a message indicating that access has been granted
            break
        #break out of the loop to end the program if the login attempt was successful
        else:
            #if the login attempt was unsuccessful, print a message indicating that access has been denied and continue the loop to prompt the user for login credentials again
            print("access denied. please try again\n")
            #print a message indicating that access has been denied and prompt the user to try again


if __name__=="__main__":
    #if the script is being run directly (not imported as a module), call the security_event_logger function to start the login process
    security_event_logger()

