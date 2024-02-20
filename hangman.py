import random

print('''
 _                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                       
''')

wordlist = ["ardvark", "baboon", "camel"]
chosen = random.randint(0, len(wordlist) - 1)
word = wordlist[chosen]
print(word)
tries = 10

def create_masked_word(word):
    length = len(word)
    masked = ""
    for i in range(length):
        masked = masked + "x"
    return masked

my_mask = create_masked_word(word)
print(f"my mask: {my_mask}")
final_word = list(my_mask)
print(f"final word: {final_word}")

while tries > 0:
    guess = input("guess letter: ")
    for i in range(0, len(word)):
        if guess == word[i]:
            guess_type = type(guess)
            final_word[i] = guess
            print(f"final word: {final_word}")
        else:
            print("wong")
    if ''.join(final_word) == word:
        print("found word")
        break
print("done")
