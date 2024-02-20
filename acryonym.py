def generate_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split())

user_phrase = input("Enter a phrase: ")
result_acronym = generate_acronym(user_phrase)
print(f"The acronym for '{user_phrase}' is: {result_acronym}")