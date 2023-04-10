arr = list(map(int, input().split()))

valid = True
for e in arr:
    if not 0 <= e <= 100:
        valid = False
        print("잘못된 점수")
        break

if valid:
    mean = sum(arr) / len(arr)
    if mean >= 80:
        print("합격")
    else:
        print("불합격")