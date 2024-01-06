from fractions import Fraction

def get_valid_decimal():
    while True:
        decimal_number = input("Enter a decimal number: ")
        try:
            decimal_number = float(decimal_number)
            return decimal_number
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")

def main():
    print("This program converts a decimal number into a fraction.")

    while True:
        decimal_number = get_valid_decimal()
        fraction_result = Fraction(decimal_number).limit_denominator()

        print(f"Decimal: {decimal_number}")
        print(f"Fraction: {fraction_result}")

        choice = input("Do you want to convert another decimal (yes/no)? ").strip().lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()
#IQDOTNET CODE - By Nelson Guajardo