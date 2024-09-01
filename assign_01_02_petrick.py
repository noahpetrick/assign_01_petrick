# Noah Petrick
# CBIS 4210
# Assignment 01-02 - Retained Earnings Calculator
# 2024-09-01

# This program will calculate the Retained Earnings of a company based on the user's input of Net Income and Dividends Paid.

def main():
    # Program greeting
    print("Hello! Welcome to your Retained Earnings Calculator.")

    # Request user's Net Income
    net_income = float(input("What was your Net Income for this year? (Enter as a number, e.g., 10000.50): "))

    # Request user's Dividends Paid
    dividends_paid = float(input("How much did you pay in Dividends this year? (Enter as a number, e.g., 5000.75): "))

    # Calculate Addition to Retained Earnings (A.R.E.)
    addition_retained_earnings = net_income - dividends_paid

    # Check if A.R.E. is negative or positive
    if are < 0:
        print("You have no Addition to Retained Earnings. You should reevaluate your financial management.")
    else:
        print(f"Great! Your Addition to Retained Earnings is: ${addition_retained_earnings:,.2f}")

        # Request Retained Earnings from last year
        retained_earnings_last_year = float(
            input("How much did you receive in Retained Earnings last year? (Enter as a number, e.g., 20000.00): "))

        # Calculate Retained Earnings for the current year
        retained_earnings_current_year = retained_earnings_last_year + addition_retained_earnings

        # Display the final Retained Earnings for the current year
        print(
            f"All done! You have accumulated ${retained_earnings_current_year:,.2f} in Retained Earnings this year. Milton Friedman would be proud!")

    # Farewell message
    print("Thank you for using the Retained Earnings Calculator. Have a great day!")


# Call the main function to run the program
if __name__ == "__main__":
    main()
