def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))
print(f"공약수: {gcd(a, b)}")