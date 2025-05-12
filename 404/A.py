alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = input();
for letter in alphabet:
    if letter not in text:
        print(letter+'\n')
        break
