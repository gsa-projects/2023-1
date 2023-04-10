n = input()

if n.isdigit():
    n = int(n)
    digits = []
    while n != 0:
        digits.insert(0, n % 1000)
        n //= 1000
    
    print(",".join(map(str, digits)))
else:
    print("입력한 값은 숫자가 아닙니다.")