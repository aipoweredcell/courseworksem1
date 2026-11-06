def unique_ip_analyser():
    #function to store, convert and manage unique ip addresses 
    ip_list=["192.168.1.1", "10.0.0.1", "92.168.1.1", "172.16.0.5", "10.0.0.1"]
    #collection of ip addresses containing duplicates

    unique_ips=set(ip_list)
    #converts the list into a set automatially removes duplicates

    print("--- Unique IP Address Analyser ---")

    print(f"\nUnique IP Address: {unique_ips}")
    #displays the unique Ip addresses in the set

    new_ip="192.168.1.50"
    unique_ips.add(new_ip)
    #adds new ip into unique ip set

    print(f"\nAfter adding {new_ip}: {unique_ips}")

    remove_ip="172.16.0.5"
    unique_ips.remove(remove_ip)
    #removes an Ip address from the set

    print(f"\nAftrer removing {remove_ip}: {unique_ips}")
    #displays updated set after remove ip was removed

    check_ip="10.0.0.1"
    if check_ip in unique_ips:
        print(f"\nCheck: '{check_ip}' exists in the set")
    else:
        print(f"\nCheck: '{check_ip}' ddoes not exist in the set")
        #checks whether a specific Ip address exists in the set using 'in'

    print(f"\nTotal number of unique Ip addresses: {len(unique_ips)}")

    return unique_ips


def main():
    unique_ip_analyser()


if __name__=="__main__":
    main()