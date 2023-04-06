import random

with open("words.txt", 'w') as file:
    for i in range(10):
        word = ''
        for _ in range(random.randint(5, 25)):  # [5, 25]
            word += chr(random.randrange(ord('a'), ord('z')))
        file.write("{}\n".format(word))

count = 0
with open("words.txt") as file:
    for w in file:
        if len(w) >= 10:
            count += 1

print(count)