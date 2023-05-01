number = input("정수 입력: ")
last = int(number[-1])

if last == 0\
		or last == 2\
		or last == 4\
		or last == 6\
		or last == 8:
	print("짝수입니다")

if last == 1\
		or last == 3\
		or last == 5\
		or last == 7\
		or last == 9:
	print("홀수입니다")
