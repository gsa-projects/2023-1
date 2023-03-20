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

import random
students = [f"{i:<3}" for i in range (1, 18)]

random.shuffle(students)

for i in range (0, len(students), 4):
    print(*students[i:i+4])