# number = 12345 # input("수를 입력: ")
# print(number) # 12345
# print(type(number)) # <class 'int'>
# print(type(type(number)))   # <class 'type'>
# print(type(type(type(number))))   # <class 'type'>
# print(type("str")(number) + "235632") # '12345'
# print(str(number)) # '12345'

# string_a = input("iuput A: ")
# int_a = int(string_a)

# string_b = input("iuput B: ")
# int_b = int(string_b)

# print("string:", string_a + string_b)
# print("int:", int_a + int_b)

# output_a = int("52.34567")
# print(output_a)

# a..z < 그리스문자 < ㄱ..ㅎ 순서임
# print('a' < 'π' < 'ㄱ')

from math import * 

# x = 89
# print(log2(x))
# print(2**ceil(log2(x)))
# print(2**ceil(log2(x)) - x)
# print()
# print(log2(2**ceil(log2(x)) - x) == int(log2(2**ceil(log2(x)) - x)))

# y = 2
# print(log2(y)) # 1.0
# print(2**ceil(log2(y))) # 2

# 4
# 100

# 3 -> 1.xx
# 2^2-1- 2^0 = 3 - 1 = 2 != 3

# 5 = 0b101
# (2^3-1) - 2^1 = 5

# 6 -> 2.xx
# (2^3-1) - 2^0 = 6
# 2^(floor(2.xx)+1) - x == 2

# 3 -> 1.xx
# 2^2-1 - 3

# 5 -> 2.xx
# 2^3-1-2^(floor(2.xx)-1) = 8 - 1 - 2 = 5 == 5

# 2 -> 1.xx
# 2^2-1 - 2^0 = 3 - 1 = 2 == 2

output = []
for x in range(1, 101):
	big = 2**(floor(log2(x)) + 1) - 1
	diff = big - x
	print(x, big, diff)
	if big > 1 and (diff != 0 and log2(diff) == int(log2(diff))):
		output.append(x)

output = [x for x in range(1, 101) if (2**(floor(log2(x)) + 1) - 1 - x != 0 and log2(2**(floor(log2(x)) + 1) - 1 - x) == int(log2(2**(floor(log2(x)) + 1) - 1 - x)))]
print(output)
