# with open("sentence.txt", 'w') as file:
#     file.write('sabcd abcd asbds ananndnd absbdbdb nanannwn mwwkwkkw oeoiiq nnnfns nsnsnn')

with open("sentence.txt") as file:
    for line in file:
        words = [e for e in line.split(' ') if 's' in e]
        for e in words:
            print(e)