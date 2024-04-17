countParts = int(input())
parts = sorted(list(map(int, input().split())))

maximum = parts[countParts - 1]
parts.pop()
summ  = sum(parts)
if maximum != summ and summ < maximum:
    print(abs(maximum - summ))
else:
    print(summ + maximum)
