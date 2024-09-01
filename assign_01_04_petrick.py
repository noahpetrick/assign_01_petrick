# Noah Petrick
# CBIS 4210
# Assignment 01-04 - Return on Total Assets Calculator and Analyst Tool
# 2024-09-01

# This program calculates the Return on Total Assets (ROA) for a company and provides an analysis of the change in ROA from last year to this year.

def calculate_roa(net_income, total_assets):
    """Calculate the Return on Total Assets (ROA)"""
    return (net_income / total_assets) * 100  # ROA as a percentage

def main():
    print("Welcome to the Return on Total Assets (ROA) Calculator and Analyst Tool!")
    # Request and calculate ROA for last year
    print("\n--- Last Year's ROA ---")
    net_income_last_year = float(input("Enter your company's Net Income last year: "))
    total_assets_last_year = float(input("Enter your company's Total Assets last year: "))
    roa_last_year = calculate_roa(net_income_last_year, total_assets_last_year)
    print(f"Your company's ROA last year was: {roa_last_year:.2f}%")

    # Request and calculate ROA for this year
    print("\n--- This Year's ROA ---")
    net_income_this_year = float(input("Enter your company's Net Income this year: "))
    total_assets_this_year = float(input("Enter your company's Total Assets this year: "))
    roa_this_year = calculate_roa(net_income_this_year, total_assets_this_year)
    print(f"Your company's ROA this year is: {roa_this_year:.2f}%")

    # Calculate the difference in ROA
    roa_change = roa_this_year - roa_last_year
    if roa_change > 0:
        print(f"\nYour ROA has increased by {roa_change:.2f}%.")
        print("It looks like your method of asset management is working. Good Job!")
    elif roa_change < 0:
        print(f"\nYour ROA has decreased by {abs(roa_change):.2f}%.")
        print("It is likely that your Net Income has declined or you have increased your Total Assets without a proportional increase to your Net Income.")
        print("You may want to focus on improving operational efficiency to boost Net Income or reassess your asset investments.")
    else:
        print("\nYour ROA has remained the same.")

     # Farewell message
    print("\nThank you for using the Return on Total Assets (ROA) Calculator and Analyst Tool!")

# Call the main function to run the program
if __name__ == "__main__":
    main()
