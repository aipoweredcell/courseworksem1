def incident_manager():
    incident= {
    "username": "admin_jdoe",
    "ip_address": "192.168.1.100",
    "event_type": "Brute Force",
    "risk_level": "High"
}
    #dictionary storing the security details

    print("--- Security Incident Manager ---")
    # Display the incident details   
    print(f"username: {incident['username']}")
    #prints the username of the incident by accessing the 'username' key in the incident dictionary.
    print(f"Ip address: {incident['ip_address']}")
    #prints the ip address of the incident by accessing the 'ip_address' key in the incident dictionary.
    incident["Status"] = "Under investigation"
    #adds a new status for key value to pair to dictionary
    incident["risk_level"] = "Critical"
    #updates exsiting risk value to critical

    del incident["event_type"]
    #deletes the element "event_type" using del 

    print("\n--- Remainging Incident Details ---")
    for key, value in incident.items():
        #loops through dictionary items to display all remainging keys and calues
        print(f"{key}: {value}")
        #counts and prints total number of key value pauirs left in the dictionary

    print(f"\nTotal number of key-value pairs: {len(incident)}")
    #couts the total number of elemetns in incident

    return incident

def main():
    incident_manager()


if __name__=="__main__":
    main()


    