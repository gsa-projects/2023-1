import random
number = random.randint(1, 100)

print("숫자를 맞혀 보세요.(1~100)")
while True:
    guess = int(input())

    if guess < number:
        print("숫자가 작습니다.")
    elif guess > number:
        print("숫자가 큽니다.")
    else:
        print("정답입니다. 입력한 숫자는 {} 입니다.".format(number))
        break