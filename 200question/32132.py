n = int(input())
word = input()
while 'PS4' in word or 'PS5' in word:
    if 'PS4' in word:
        word = word.replace('PS4', 'PS')
    if 'PS5' in word:
        word = word.replace('PS5', 'PS')
print(word)