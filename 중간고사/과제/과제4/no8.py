def testPrime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(2, 100 + 1):
    if testPrime(i):
        print(i)