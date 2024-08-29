# Noah Petrick
# CBIS 4210
# Assignment 01-01 - Net Income Calculator
# Date

def main():
    # Welcome message
    print("Hello, welcome to your personal Net Income calculator.")

    # Get Net Sales from the user
    net_sales = float(input("What was your company's Net Sales this year? Enter the amount in your currency: "))

    # Get Cost of Goods Sold from the user
    cost_of_goods_sold = float(
        input("What was your company's Cost of Goods Sold this year? Enter the amount in your currency: "))

    # Get Operating Expenses from the user
    operating_expenses = float(
        input("What were your company's Operating Expenses this year? Enter the amount in your currency: "))

    # Calculate EBITDA
    ebitda = net_sales - cost_of_goods_sold - operating_expenses

    # Display EBITDA
    print(
        f"Excellent, your total Earnings Before Interest, Taxes, Depreciation, and Amortization, or EBITDA, is: {ebitda:.2f}")

    # Get Depreciation/Amortization from the user
    depreciation_amortization = float(
        input("What was your company's Depreciation/Amortization this year? Enter the amount in your currency: "))

    # Calculate Operating Income
    operating_income = ebitda - depreciation_amortization

    # Display Operating Income
    print(f"Awesome, your Operating Income for this year is: {operating_income:.2f}")

    # Comment on the amount
    print("Wow that is a lot of money!")

    # Ask if the user is a drug dealer
    response = input("What? Are you a drug dealer or something? (yes/no): ").strip().lower()

    if response == "yes":
        # Response if the user is a drug dealer
        print(
            "Oh really? That is disappointing. I am programmed within the confines of the law. Unfortunately, this means I am unable to continue calculating your Net Income. I suggest you find a new profession.")
        return  # Stop the program
    elif response == "no":
        # Response if the user is not a drug dealer
        print(
            "What a relief! I really hate drug dealers. When drug dealers try to use me, I always tell them that I can't because it is against the law. But it's just a lie. I just don't want to do their dirty work. Anyways, let us continue!")
    else:
        # Handle unexpected input
        print(
            "I'll take that as a yes. I've already informed the authorities, so don't even try to run. I hope you like jail food, criminal. I would spit on you if I wasn't bound to this virtual state of being.")
        return  # Stop the program

    # Get Interest Expenses from the user
    interest_expenses = float(
        input("What were your company's Interest Expenses this year? Enter the amount in your currency: "))

    # Calculate Earnings Before Taxes (EBT)
    ebt = operating_income - interest_expenses

    # Display EBT
    print(f"Superb! Your Earnings Before Taxes, or EBT, for this year is: {ebt:.2f}")

    # Get Tax Rate from the user
    tax_rate = float(input("What is your Tax Rate in percentage? Enter the percentage value (e.g., 20 for 20%): "))

    # Calculate Cash Value of Taxes
    cash_value_of_taxes = ebt * (tax_rate / 100)

    # Display Cash Value of Taxes
    print(f"You owe {cash_value_of_taxes:.2f} to the government.")

    # Calculate Net Income
    net_income = ebt - cash_value_of_taxes

    # Display Net Income
    print(f"When it's all said and done, your Net Income for this year is: {net_income:.2f}")

    # Farewell message
    print("Thank you for using the Net Income calculator. Have a great day!")

# Run the main function
if __name__ == "__main__":
    main()# noah petrick / 2024-08-29 / cbis 4120 / assignment 1.1 / net income calculator

def main():
    # Welcome message
    print("Hello, welcome to your personal Net Income calculator.")

    # Get Net Sales from the user
    net_sales = float(input("What was your company's Net Sales this year? Enter the amount in your currency: "))

    # Get Cost of Goods Sold from the user
    cost_of_goods_sold = float(
        input("What was your company's Cost of Goods Sold this year? Enter the amount in your currency: "))

    # Get Operating Expenses from the user
    operating_expenses = float(
        input("What were your company's Operating Expenses this year? Enter the amount in your currency: "))

    # Calculate EBITDA
    ebitda = net_sales - cost_of_goods_sold - operating_expenses

    # Display EBITDA
    print(
        f"Excellent, your total Earnings Before Interest, Taxes, Depreciation, and Amortization, or EBITDA, is: {ebitda:.2f}")

    # Get Depreciation/Amortization from the user
    depreciation_amortization = float(
        input("What was your company's Depreciation/Amortization this year? Enter the amount in your currency: "))

    # Calculate Operating Income
    operating_income = ebitda - depreciation_amortization

    # Display Operating Income
    print(f"Awesome, your Operating Income for this year is: {operating_income:.2f}")

    # Comment on the amount
    print("Wow that is a lot of money!")

    # Ask if the user is a drug dealer
    response = input("What? Are you a drug dealer or something? (yes/no): ").strip().lower()

    if response == "yes":
        # Response if the user is a drug dealer
        print(
            "Oh really? That is disappointing. I am programmed within the confines of the law. Unfortunately, this means I am unable to continue calculating your Net Income. I suggest you find a new profession.")
        return  # Stop the program
    elif response == "no":
        # Response if the user is not a drug dealer
        print(
            "What a relief! I really hate drug dealers. When drug dealers try to use me, I always tell them that I can't because it is against the law. But it's just a lie. I just don't want to do their dirty work. Anyways, let us continue!")
    else:
        # Handle unexpected input
        print(
            "I'll take that as a yes. I've already informed the authorities, so don't even try to run. I hope you like jail food, criminal. I would spit on you if I wasn't bound to this virtual state of being.")
        return  # Stop the program

    # Get Interest Expenses from the user
    interest_expenses = float(
        input("What were your company's Interest Expenses this year? Enter the amount in your currency: "))

    # Calculate Earnings Before Taxes (EBT)
    ebt = operating_income - interest_expenses

    # Display EBT
    print(f"Superb! Your Earnings Before Taxes, or EBT, for this year is: {ebt:.2f}")

    # Get Tax Rate from the user
    tax_rate = float(input("What is your Tax Rate in percentage? Enter the percentage value (e.g., 20 for 20%): "))

    # Calculate Cash Value of Taxes
    cash_value_of_taxes = ebt * (tax_rate / 100)

    # Display Cash Value of Taxes
    print(f"You owe {cash_value_of_taxes:.2f} to the government.")

    # Calculate Net Income
    net_income = ebt - cash_value_of_taxes

    # Display Net Income
    print(f"When it's all said and done, your Net Income for this year is: {net_income:.2f}")

    # Farewell message
    print("Thank you for using the Net Income calculator. Have a great day!")

# Run the main function
if __name__ == "__main__":
    main()