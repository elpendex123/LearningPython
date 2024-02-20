def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        # Initialize the first two numbers in the Fibonacci sequence
        fib_sequence = [1, 1]

        # Calculate the Fibonacci sequence up to the nth number
        for _ in range(2, n):
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)

        # The nth Fibonacci number is the last number in the sequence
        return fib_sequence[-1]

# Input: User provides the value of n
n = int(input("Enter the value of n for the Fibonacci sequence: "))

# Calculate the nth Fibonacci number
result = fibonacci(n)

# Output the result
print(f"The {n}th Fibonacci number is: {result}")
