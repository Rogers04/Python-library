# Example of using sets

letters = set()

while True: 
    letter = input('Enter: ')
    letters.add(letter.lower())

    if 'l' in letters:
        print('Congratulations')
        break

    print(letters)