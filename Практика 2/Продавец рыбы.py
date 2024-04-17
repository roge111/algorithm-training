countDaysF, countDays = map(int, input().split())
data = list(map(int, input().split()))
end = len(data) - 1 - countDays
maximum = 0
for i in range(len(data)-1):
    if i <= end:
        for j in range(i+1,i + countDays + 1):
            # t_1 = data[j]
            # t_2 = data[i]
            if data[j] - data[i] > maximum:
                maximum = data[j] - data[i]
    else:
        for j in range(i+1, len(data)):
            if data[j] - data[i] > maximum:
                maximum = data[j] - data[i]
print(maximum)