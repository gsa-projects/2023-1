def weeklyPay(rate, hour):
    overtime = max(0, hour - 30)
    return 1.5 * rate * overtime + rate * (hour - overtime)

rate = int(input("시급 입력: "))
hour = int(input("근무 시간: "))
print("주급은 {}".format(weeklyPay(rate, hour)))