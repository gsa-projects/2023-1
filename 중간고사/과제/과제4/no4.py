a = input("a> ")
b = input("b> ")
dicA = dict()
dicB = dict()

for c in a:
    if c not in dicA:
        dicA[c] = 0
    dicA[c] += 1

for c in b:
    if c not in dicB:
        dicB[c] = 0
    dicB[c] += 1

if dicA == dicB:
    print("YES")
else:
    print("NO")