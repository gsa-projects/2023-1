number = int(input())

a = number % 10
number //= 10
b = number % 10
number //= 10
c = number % 10
number //= 10
d = number % 10
number //= 10
e = number % 10

print(a + b + c + d + e)