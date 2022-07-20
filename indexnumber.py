wordx = input("Enter any word: ")
vowels = ['A','E','I','O','U','Y','a','e','i','o','u','y']

print(f'Original String is {wordx}')
print('Printing only even index chars')
for i in wordx:
    if i not in vowels:

        print(i)
        
# ------------------------------------------

# word = input('Enter word: ') ---> pynative for work
# print('Original String', word)

# size = len(word)
# print('Print only even index char')

# for i in range(0, size - 1, 2):
#     print('index[', i, ']', word[i])