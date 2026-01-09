'''
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
'''
import os

secret = 'heart'
letters_corrent = ''
attempts_numbers = 0

while True:
    digit_letter = input('Type a letter: ')
    attempts_numbers += 1
    
    if len(digit_letter) > 1: 
        print('TYPE JUST ONLY LETTER.')
        continue
    
    if digit_letter in secret:
        letters_corrent += digit_letter

    formed_word = ''
    for secret_letters in secret:
        if secret_letters in letters_corrent:
            formed_word += secret_letters

        else: 
            formed_word += '*'
    
    print('Formed word: ', formed_word)

    if formed_word == secret:
        os.system('cls')        
        print('YOU IN CHAMP!')
        print('Secret word was: ', secret)
        print(f'You attempt: {attempts_numbers}x')
        letters_corrent = ''
        attempts_numbers = 0
