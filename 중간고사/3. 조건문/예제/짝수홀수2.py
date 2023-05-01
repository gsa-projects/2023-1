number = input("정수 입력: ")
last = number[-1]

if last in "02468":
	print("짝수입니다")

if last in "13579":
	print("홀수입니다")
