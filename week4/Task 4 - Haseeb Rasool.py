def validate_ip(ip):
    ip = ip.strip()
    # strips whitespace before and after from the ip string

    if "." not in ip:
        return False
    # returns false if there are no dots in ip

    if ip.count(".") != 3:
        # checks if ip address has exactly 3 dots
        return False

    parts = ip.split(".")
    # splits the ip address string into a list of parts from the dots

    if len(parts) != 4:
        # counts that the split resulted in 4 parts
        return False

    for part in parts:
        if not part.isdigit():
            return False

        number = int(part)
        if number < 0 or number > 255:
            return False

    return True


def main():
    print("--- ip address validator ---")

    while True:
        try:
            ip_address = input("enter an ip address: ")

            if validate_ip(ip_address):
                print("valid ip address\n")
                break
            else:
                print("invalid ip address\n")
                
        except Exception as e:
            #catches unexpected during input or execution
            print(f"An error has occured as {e}. please try again.\n")


if __name__ == "__main__":
    main()