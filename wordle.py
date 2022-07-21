secret = 'candy'
# typed = []
letters = ['c','a','n','d','y']

while True:
    word = input('Type a 5 letter word: ')
    if len(word) != 5:
        print('You need to type a 5 letter word.')
        continue

# need to fix this below
    # for letter in secret:
    #     if letter in word and letters: 
    #         print(f'There is {letters}.')
    #     else:
    #         break
# need to fix this above

    # typed.append(word)
    
    # for secret_letter in secret:
    #     if secret_letter in word and len(word) == letters:
    #         print(f'There is {secret_letter}')
    #     else:
    #         break

    # secret_temp = ''
    # for secret_letter in secret:
    #     if secret_letter in word:
    #         secret_temp += secret_letter
    #     else:
    #         secret_temp += '*'

    if word != secret:
        print('Try again.')
        continue
    else:
        print('You won.')
        break
