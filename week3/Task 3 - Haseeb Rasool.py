def security_event_analysis():
    # This function analyzes a security event log and extracts relevant information such as failed login attempts, login events, and the IP address involved.
    event_text = "security alert: Failed login attempt detected from Ip address 192.168.1.25. the user account admin was targeted at 22:45. the server blocked the login attempt after an incorrect password was entered."
    #variable to store the status of failed login attempts
    
    print("Security Event Analysis:")
    #display a separator line for better readability
    print("-" * 24)
    #print the original event text for reference

    if "Failed" in event_text:
        #set the failed_status variable to "yes" if a failed login attempt is detected in the event text
        failed_status="yes"
        #print a warning message indicating that a failed security event was detected
    else:
        #set the failed_status variable to "no" if no failed login attempt is detected in the event text
        failed_status="no"
        #print a message indicating that no failed security event was detected


    if "login" in event_text:
        #set the login_status variable to "yes" if a login event is detected in the event text
        login_status="yes"
        #print a message indicating that a login event was detected
    else:
        #set the login_status variable to "no" if no login event is detected in the event text
        login_status="no"
        #print a message indicating that no login event was detected


    words=event_text.split()
    #initialize a variable to store the IP address
    ip_address = ""
    #loop through the words in the event text to find the IP address
    for i in range(len(words)):
        #check if the current word is "address" and if so, extract the next word as the IP address
        if words[i] =="address":
            #extract the IP address from the next word and remove any trailing period
            ip_address=words[i + 1].rstrip('.')
            #
            break
            #break the loop once the IP address is found to avoid unnecessary iterations

    print(f"Failed event; {failed_status}")
    #print the status of failed login attempts
    print(f"login event: {login_status}")
    #print the status of login events
    print(f"Ip address:{ip_address}")
    #print the extracted IP address involved in the security event

    if failed_status == "yes":
        #if a failed login attempt was detected, print a warning message and indicate that an investigation is needed
        print("warning: a failed security event was deteced")
        #print a message indicating that an investigation is needed for the failed login attempts
    if login_status == "yes":
        #if a login event was detected, print a message indicating that a login was detected and that an investigation is needed
        print("login detected")
        #print a message indicating that an investigation is needed for the login events

    print("Action: investigate the failed login attempts")
    #print a message indicating that an investigation is needed for the failed login attempts

if __name__ == "__main__":
        #call the security_event_analysis function to execute the analysis when the script is run directly
        security_event_analysis()