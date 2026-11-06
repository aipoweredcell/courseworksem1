def incident_record():
    #function to store the incident record information in a tuple
    information=("admin",
                 "ip",
                 "event_type",
                 "severity",
                 )
    #tuple storing information about the incident record

    print("--- Security Incident Record ---")


    print(f"\nUsername: {information[0]}")
    #prints the username from the tuple
    print(f"\nIp: {information[1]}")
    #prints the ip from the tuple
    print(f"\nEvent Type: {information[2]}")
    #prints the event type from the tuple
    print(f"\nSeverity: {information[3]}")
    #prints the severity from the tuple

    print(f"\nTotal amounts of elements in the tuple: {len(information)}")
    #prints the total number of elements in the tuple
    
    target_event="Unauthorized Access"
    #checks if the target event is present in the tuple and prints the result
    if target_event in information:
        #if the target event is found in the tuple, print a message indicating it was found
        print(f"Check: '{target_event}' was found in the record")
        #if the target event is not found in the tuple, print a message indicating it was not found
    else:
        #else block to handle the case when the target event is not found in the tuple
        print(f"Check: '{target_event}' was not found" )
        #print a message indicating that the target event was not found in the record

    print(f"\n--- Testing the tuple ---")
    #test the immutability of the tuple by attempting to modify one of its elements
    try:
        #attempt to modify the severity element of the tuple, which should raise a TypeError
        information[3] = "Critical"
        #if the modification is successful, print a message indicating that the tuple was modified
    except TypeError as e:
        #catch the TypeError and print a message indicating that the tuple cannot be modified
        print(f"Caught expected error: {e}")
        #print a message indicating that the tuple cannot be modified, keeping incident logs secure
        print("Observation: Tuples cannot be mopdified, keeping incident logs secure")
        #print a message indicating that the tuple cannot be modified, keeping incident logs secure

    return information
    #returns the tuple containing the incident record information

def main():
    #calls the incident_record function to store and print the incident record information
    incident_record()


if __name__ == "__main__":
    #calls the main function to execute the program
    main()
