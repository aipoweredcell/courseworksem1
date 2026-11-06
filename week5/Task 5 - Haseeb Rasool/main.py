import security_tools

def main():
    print(" === Cyber security utility toools ---")

    user_password=input("Please enter a password to validate: ")
    user_ip = input("Enter an Ip address to validate: ")

    print("\n--- Validation results")

    is_password_valid=security_tools.validate_password(user_password)
    if is_password_valid:
        print(f"Password '{user_password}': VALID (Strong)")
    else:
        print(f"Password '{user_password}': INVALID (weak or too short)")
        suggested_password=security_tools.generate_strong_password()
        print(f"P-> Suggested strong password: {suggested_password}")

    is_ip_valid=security_tools.validate_ip(user_ip)
    if is_ip_valid:
        print(f"IP address '{user_ip}': VALID format")
    else:
        print(f"IP address '{user_ip}': INVALID format")



if __name__=="__main__":
    main()
