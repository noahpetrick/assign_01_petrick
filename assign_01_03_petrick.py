# Noah Petrick
# CBIS 4210
# Assignment 01-03 - Cash Flow Evaluator
# 2024-09-01

def main():
    # Greet the user
    print("Welcome to the Cash Flow Evaluator!")

    # Operating Activities
    print("\n--- Operating Activities ---")
    cash_from_sales = float(input("Enter cash received from sales: "))
    cash_from_services = float(input("Enter cash received from services: "))
    cash_paid_to_suppliers = float(input("Enter cash paid to suppliers: "))
    cash_paid_to_employees = float(input("Enter cash paid to employees: "))
    cash_paid_for_taxes = float(input("Enter cash paid for taxes: "))

    net_cash_operating = (cash_from_sales + cash_from_services) - (
                cash_paid_to_suppliers + cash_paid_to_employees + cash_paid_for_taxes)
    print(f"Net Cash from Operating Activities: ${net_cash_operating:,.2f}")

    # Investing Activities
    print("\n--- Investing Activities ---")
    cash_paid_for_ppe = float(input("Enter cash paid for property, plant, and equipment: "))
    cash_received_from_investments = float(input("Enter cash received from selling investments: "))

    net_cash_investing = cash_received_from_investments - cash_paid_for_ppe
    print(f"Net Cash from Investing Activities: ${net_cash_investing:,.2f}")

    # Financing Activities
    print("\n--- Financing Activities ---")
    cash_from_issuing_stock = float(input("Enter cash received from issuing stock: "))
    cash_from_borrowing = float(input("Enter cash received from borrowing: "))
    cash_paid_for_dividends = float(input("Enter cash paid for dividends: "))
    cash_paid_for_debt = float(input("Enter cash paid for repaying debt: "))

    net_cash_financing = (cash_from_issuing_stock + cash_from_borrowing) - (
                cash_paid_for_dividends + cash_paid_for_debt)
    print(f"Net Cash from Financing Activities: ${net_cash_financing:,.2f}")

    # Total Net Cash Flow
    total_net_cash_flow = net_cash_operating + net_cash_investing + net_cash_financing
    print(f"\n--- Total Net Cash Flow ---")
    print(f"Total Net Cash Flow: ${total_net_cash_flow:,.2f}")

    # Evaluate the cash flow
    if total_net_cash_flow > 0:
        print("Your company has a positive cash flow. Well done!")
    elif total_net_cash_flow < 0:
        print("Your company has a negative cash flow. You may need to review your finances.")
    else:
        print("Your company has a neutral cash flow. No gain, no loss.")

    # Farewell message
    print("Thank you for using the Cash Flow Evaluator. Have a great day!")

# Call the main function to run the program
if __name__ == "__main__":
    main()
