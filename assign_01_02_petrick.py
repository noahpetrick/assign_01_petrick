# Noah Petrick
# CBIS 4210
# Assignment 01-02 - Retained Earnings Calculator
# Date

def main():
    # Step 1: Program greeting
    print("Hello! Welcome to your Retained Earnings Calculator.")

    # Step 2: Request user's Net Income
    net_income = float(input("What was your Net Income for this year? (Enter as a number, e.g., 10000.50): "))

    # Step 3: Request user's Dividends Paid
    dividends_paid = float(input("How much did you pay in Dividends this year? (Enter as a number, e.g., 5000.75): "))

    # Step 4: Calculate Addition to Retained Earnings (A.R.E.)
    are = net_income - dividends_paid

    # Step 5: Check if A.R.E. is negative or positive
    if are < 0:
        print("You have no Addition to Retained Earnings. You should reevaluate your financial management.")
    else:
        print(f"Great! Your Addition to Retained Earnings is: ${are:,.2f}")

        # Step 6: Request Retained Earnings from last year
        retained_earnings_last_year = float(
            input("How much did you receive in Retained Earnings last year? (Enter as a number, e.g., 20000.00): "))

        # Step 7: Calculate Retained Earnings for the current year
        retained_earnings_current_year = retained_earnings_last_year + are

        # Step 8: Display the final Retained Earnings for the current year
        print(
            f"All done! You have accumulated ${retained_earnings_current_year:,.2f} in Retained Earnings this year. Milton Friedman would be proud!")


# Call the main function to run the program
if __name__ == "__main__":
    main()
