countBerries = int(input())
heightMax = 0
height = 0
data = {}
for i in range(countBerries):
    up, down = map(int, input().split())
    if up in data:
        data[up].append([down, i+1])
    else:
        data[up] = [[down, i+1]]
data_key = sorted(data)[::-1]

way = []
for up_key in data_key:
    days = sorted(data[up_key])
    for day in days:
        height += up_key
        if height > heightMax:
            heightMax = height
        height -= day[0]
        way.append(day[1])
print(heightMax)
for number in way:
    print(number, end=' ')









# data = []
# for i in range(countBerries):
#     up, down = map(int, input().split())
#     data.append([up, down, i+1])
# data = sorted(data)[::-1]
# way = []
# for day in data:
#     height += day[0]
#     if height > heightMax:
#         heightMax = height
#     way.append(day[2])
#     height -= day[1]
# print(heightMax)
# for number in way:
#     print(number, end=' ')