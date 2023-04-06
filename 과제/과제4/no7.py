def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))
print("공약수: {}".format(gcd(a, b)))
