import random

numbers = "0123456789"
symbols = "!#$%&()*+"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
letters = lower + upper

all = letters + numbers + symbols

num_letters = int(input("letters: "))
num_numbers = int(input("numbers: "))
num_symbols = int(input("symbols: "))

final_word = ""
for n in range(1, num_letters + 1):
    mystring = letters[random.randint(0, len(letters) - 1)]
    final_word += mystring
print(final_word)

numbers_random = random.sample(numbers, num_numbers)
for random_num in numbers_random:
    final_word += random_num
print(final_word)

symbols_random = random.sample(symbols, num_symbols)
for random_sym in symbols_random:
    final_word += random_sym
print(final_word)

shuffled = list(final_word)
random.shuffle(shuffled)
print(f"shuffled: {shuffled}")
joined = ''.join(shuffled)
print(f"joined: {joined}")


# CHAT GPT'S SOLUTION:
# def generate_password():
#     # Define the pool of characters
#     letters_lower = string.ascii_lowercase
#     letters_upper = string.ascii_uppercase
#     digits = string.digits
#     symbols = string.punctuation
#
#     # Generate random characters from each pool
#     password = ([random.choice(letters_lower) for _ in range(5)] +
#                 [random.choice(letters_upper) for _ in range(5)] +
#                 [random.choice(digits) for _ in range(2)] +
#                 [random.choice(symbols) for _ in range(2)])
#
#     # Shuffle the characters to randomize the password
#     random.shuffle(password)
#
#     # Convert the list of characters to a string
#     return ''.join(password)
#
# # Generate and print the random password
# random_password = generate_password()
# print(f"Generated Password: {random_password}")
