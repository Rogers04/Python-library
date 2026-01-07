phrase = 'O Python é uma linguagem de programação'\
    'multiparadigma.' \
    'Python foi criado por Guido van Rossum.'

i = 0

amount_of_letters = 0
letters_appeared_more = ''

while i < len(phrase):
    current_letter = phrase[i]
    letter_appeared = phrase.count(current_letter)


    if current_letter == ' ':
        i += 1
        continue


    amount_letters = phrase.count(current_letter)

    if amount_of_letters < amount_letters:
        amount_of_letters = amount_letters
        letters_appeared_more = current_letter

    i += 1

print(
    'The letter that appeared most often was '
    f'"{letters_appeared_more}" that appeared ' 
    f'{amount_of_letters}x'
)