def calculate_failed_percentage(failed_logins, total_logins):
    # Defines a function that accepts failed and total login counts.
    failed_percentage = (failed_logins / total_logins) * 100
    return failed_percentage


def main():
    print("--- Failed login risk calculator ---")

    while True:
        # Starts loop to keep prompting until valid numbers are inputted.
        try:
            failed_logins = int(input("Enter number of failed login attempts: "))
            #failed logins asks for input and stores as variable
            total_logins = int(input("Enter total number of login attempts: "))

            if failed_logins > total_logins:
                #puts an if for if the failed amount is greater than total amount
                print("Error: failed attempts cannot be greater than total attempts.\n")
                continue

            percentage = calculate_failed_percentage(failed_logins, total_logins)
            #calls functuion to compute failure percentage
            print(f"Failed login percentage: {percentage:.2f}%")
            #prints the percentage formatted to dec places

            if percentage >= 50:
                #if percentage is 50 or more then it prints risk level high
                print("Risk level: HIGH RISK\n")
            elif percentage >= 25:
                #elif the percentage is 25 orm more then medium
                print("Risk level: MEDIUM RISK\n")
            else:
                print("Risk level: LOW RISK\n")

            break

        except ValueError:
            #if numbers are noot enterred then prints error message
            print("Please enter numbers only.\n")

        except ZeroDivisionError:
            #if no attempts were made prints error message
            print("Total login attempts cannot be zero.\n")


if __name__ == "__main__":
    main()