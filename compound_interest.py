def calculate_compound_interest(principal, interest_rate, time, frequency):
    # Convert interest rate to a decimal
    interest_rate_decimal = interest_rate / 100
    # Calculate compound interest
    final_amount = principal * (1 + (interest_rate_decimal / frequency)) ** (frequency * time)
    return final_amount

# Example usage with predefined values
principal_amount = 1000  # Example principal amount
interest_rate_percent = 1  # Example interest rate in percentage
years = 5  # Example number of years
interest_frequency = 12  # Example interest frequency (monthly)

# Calculate and print compound interest
result = calculate_compound_interest(principal_amount, interest_rate_percent, years, interest_frequency)
print(f"Final amount after {years} years: ${result:.2f}")

# User input for custom values
user_principal = float(input("Enter the principal amount: "))
user_interest_rate = float(input("Enter the interest rate (in percentage): "))
user_years = float(input("Enter the number of years: "))
user_frequency = float(input("Enter the interest frequency per year: "))

# Calculate and print compound interest with user input
user_result = calculate_compound_interest(user_principal, user_interest_rate, user_years, user_frequency)
print(f"Final amount after {user_years} years: ${user_result:.2f}")
