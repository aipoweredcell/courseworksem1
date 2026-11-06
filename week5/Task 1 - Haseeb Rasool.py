def suspicious_ip():
#function to create a list of suspicous ips
    suspicious_ips=[
    "192.168.1.10",
    "10.0.0.5",
    "172.16.4.20",
    "192.168.100.50",
    "203.0.113.15",
    ]
    #create a list of suspicious IP addresses

    print("--- initial suspicious IP List ---")
    print(suspicious_ips)

    print(f"\nFirst ip address in the list: {suspicious_ips[0]}")
    #prints the first ip address in the list
    print(f"\nLast ip address in the list: {suspicious_ips[-1]}")
    #prints the last ip address in the list

    print("\n--- Add a New IP Address ---")
    #prints a message to the user to add a new ip address
    new_ip=input("Enter a new suspicious IP address to add: ")
    #variable to store the new ip address entered by the user

    suspicious_ips.append(new_ip)
    #adds the new ip address to the list
    print(f"Updated list after adding {new_ip}:")
    #prints a message to the user showing the updated list after adding the new ip address
    print(suspicious_ips)
    #prints the updated list of suspicious ip addresses

    print("\n--- Modify an Existing IP Address ---")
    #prints a message to the user to modify an existing ip address
    old_ip=input("Enter an IP address you want to change: ")
    #variable to store the old ip address entered by the user
    if old_ip in suspicious_ips:
        #finds the index of the old ip address in the list and replaces it with the new ip address entered by the user
        index= suspicious_ips.index(old_ip)
        #variable to store the new replacement ip address entered by the user
        replacement_ip=input("Enter the new replacement ip address: ")
        #replaces the old ip address with the new replacement ip address in the list
        suspicious_ips[index]=replacement_ip
        #prints a message to the user showing the updated list after modifying the ip address
        print(f"successfully updated! New list: {suspicious_ips}")
        #prints the updated list of suspicious ip addresses
    else:
        #else statement to handle the case where the old ip address is not found in the list
        print("Error: that ip address was not found in the list.")
        #prints an error message to the user indicating that the old ip address was not found in the list

    print("\n--- Total Number of IP Addresses ---")
    #prints the total number of ip addresses in the list
    print(f"Total count: {len(suspicious_ips)}")
    #prints the total number of ip addresses in the list

    print("\n--- Search for an IP Address ---")
    #prints a message to the user to search for an ip address in the list
    search_ip=input("Enter an IP address to search for: ")
    #variable to store the ip address entered by the user to search for in the list
    if search_ip in suspicious_ips:
        #if statement to check if the ip address entered by the user is in the list
        print(f"Result: The IP address '{search_ip}' EXISTS in the list.")
        #prints a message to the user indicating that the ip address entered by the user exists in the list
    else:
        #else statement to handle the case where the ip address entered by the user is not found in the list
        print(f"Result: the IP address '{search_ip}' does NOT exist in the list")
        #prints a message to the user indicating that the ip address entered by the user does not exist in the list

        return suspicious_ip
    #returns the list of suspicious ip addresses

def main():
    #main function to call the suspicious_ip function
    suspicious_ip()

if __name__ =="__main__":
    #calls the main function to run the program
    main()