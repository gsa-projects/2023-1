x = int(input())
y = int(input())

print(f"({x}, {y})")

if x > 0:
	if y > 0:
		print("1")
	else:
		print("4")
else:
	if y > 0:
		print("2")
	else:
		print("3")
