def recursive_gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))
print("공약수: {}".format(gcd(a, b)))
