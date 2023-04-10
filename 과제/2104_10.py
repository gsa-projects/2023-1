with open("sentence.txt") as file:
    for line in file:
        words = [e.strip(",.[]“”()") for e in line.split() if 's' in e]
        for w in words:
            print(w)