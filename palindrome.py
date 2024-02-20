def is_palindrome(input_str):
    # Function to remove spaces and punctuation, and convert to lowercase
    def preprocess_string(s):
        return ''.join(char.lower() for char in s if char.isalnum())

    # Function to check if a string is a palindrome
    def check_palindrome(s):
        stack = []
        for char in s:
            stack.append(char)
        reversed_str = ''.join(stack[::-1])
        return s == reversed_str

    processed_str = preprocess_string(input_str)
    return check_palindrome(processed_str)

# Test cases
print(is_palindrome("radar"))  # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("hello"))  # False
