limit = 10000
i = 1
sum = i

while sum <= limit:
    i += 1
    sum += i

print("{}을 더할 때 {}을 넘으며 그 때의 값은 {}입니다.".format(i, limit, sum))