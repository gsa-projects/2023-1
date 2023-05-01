num = input()
digits = []
valid = True

for c in num:
    if not c.isdigit():
        valid = False
        print("입력한 값은 숫자가 아닙니다.")
        break

if valid:
    num = int(num)
    while num != 0:
        digits.insert(0, num % 1000)
        num //= 1000

    digits = list(map(str, digits))
    print(','.join(digits))