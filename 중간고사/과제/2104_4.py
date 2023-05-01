marks = [90, 25, 67, 45, 80]

for i, mark in enumerate(marks):
	if mark >= 60:
		print(f"{i+1}번 학생은 합격입니다.")
	else:
		print(f"{i+1}번 학생은 불합격입니다.")