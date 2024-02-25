def binary_to_decimal(binary):
    decimal = 0
    position = 0

    # Iterate through each digit in the binary number
    for digit in reversed(str(binary)):
        # Convert the digit to an integer and add its positional value to the decimal
        decimal += int(digit) * (2 ** position)
        position += 1

    return decimal

# Input: User provides a binary number
binary_input = input("Enter a binary number: ")

try:
    # Convert the binary number to decimal
    result_decimal = binary_to_decimal(binary_input)
    print(f"The decimal equivalent of {binary_input} is: {result_decimal}")
except ValueError:
    print("Invalid input. Please enter a binary number (0s and 1s only).")
