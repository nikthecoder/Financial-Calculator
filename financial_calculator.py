import math

def calculate_mortgage_payment(principal, annual_rate, years):
    monthly_rate = (annual_rate / 12) / 100
    num_payments = years * 12
    mortgage_payment = principal * (monthly_rate / (1 - (1 + monthly_rate) ** -num_payments))
    return mortgage_payment

def calculate_retirement_balance(principal, annual_rate, years):
    monthly_rate = (annual_rate / 12) / 100
    num_payments = years * 12
    retirement_balance = principal * ((1 + monthly_rate) ** num_payments)
    return retirement_balance

def calculate_time_to_double(principal, annual_rate):
    monthly_rate = (annual_rate / 12) / 100
    time_to_double = math.log(2) / math.log(1 + monthly_rate)
    return time_to_double

def calculate_rate_of_growth(starting_value, ending_value, time):
    rate_of_growth = ((ending_value / starting_value) ** (1 / time) - 1) * 100
    return rate_of_growth

def solve_logarithmic_equation(base, result):
    # Solves equations in the form base^x = result, where x is the unknown.
    # The function returns the value of x.
    return math.log(result, base)

def to_scientific_notation(number, precision=2):
    # Convert a number to scientific notation as a string.
    notation = f"{number:.{precision}e}"
    return notation

def from_scientific_notation(scientific_notation):
    # Convert a number from scientific notation (string) to a float.
    return float(scientific_notation)


def main():
    while True:
        print("Choose a financial calculation:")
        print("1. Calculate Monthly Mortgage Payment")
        print("2. Estimate Retirement Account Balance")
        print("3. Determine Time Required to Double Money")
        print("4. Calculate Rate of Growth")
        print("5. Solve Logarithmic Equations")
        print("6. Convert to Scientific Notation")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            # Description: Calculate the monthly mortgage payment.
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the annual interest rate (%): "))
            time = float(input("Enter the number of years: "))
            mortgage_payment = calculate_mortgage_payment(principal, rate, time)
            print("Your monthly mortgage payment is:", mortgage_payment)

        elif choice == '2':
            # Description: Estimate the retirement account balance at the time of retirement.
            principal = float(input("Enter the initial investment: "))
            rate = float(input("Enter the annual rate of return (%): "))
            time = float(input("Enter the number of years until retirement: "))
            retirement_balance = calculate_retirement_balance(principal, rate, time)
            print("Your retirement account balance at retirement is:", retirement_balance)

        elif choice == '3':
            # Description: Determine the time required for an investment to double, given the rate.
            principal = float(input("Enter the initial investment: "))
            rate = float(input("Enter the annual rate of return (%): "))
            time_to_double = calculate_time_to_double(principal, rate)
            print("It will take approximately", time_to_double, "years to double your money.")

        elif choice == '4':
            # Description: Calculate the rate of growth.
            starting_value = float(input("Enter the starting value: "))
            ending_value = float(input("Enter the final value: "))
            time = float(input("Enter the number of years: "))
            rate_of_growth = calculate_rate_of_growth(starting_value, ending_value, time)
            print("The rate of growth is approximately", rate_of_growth, "% per year.")

        elif choice == '5':
            # Description: Solve logarithmic equations.
            base = float(input("Enter the base of the logarithmic equation: "))
            result = float(input("Enter the result of the logarithmic equation: "))
            x = solve_logarithmic_equation(base, result)
            print(f"The solution to {base}^x = {result} is x = {x}")

        elif choice == '6':
            # Description: Convert numbers to and from scientific notation.
            print("1. Convert to Scientific Notation")
            print("2. Convert from Scientific Notation")
            sub_choice = input("Enter your choice (1/2): ")
            if sub_choice == '1':
                number = float(input("Enter the number for scientific notation conversion: "))
                scientific = to_scientific_notation(number)
                print(f"{number} in scientific notation is {scientific}")
            elif sub_choice == '2':
                scientific_notation = input("Enter a number in scientific notation (e.g., 1.23e4): ")
                original_number = from_scientific_notation(scientific_notation)
                print(f"Back to the original number: {original_number}")

        elif choice == '7':
            print("Exiting the financial app. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
