def bin_search(value: int, cnt_reg: int):
    l, r = -1, countRegiments+1
    while l < r - 1:
        mid = (l+r)//2
        if mid+ cnt_reg >= countRegiments+ 1 or prefix_sum[mid+cnt_reg] - prefix_sum[mid] > value:
            r = mid
        else:
            l = mid
    if l >=0 and l < countRegiments + 1 and l + cnt_reg < countRegiments + 1 and prefix_sum[l+cnt_reg] - prefix_sum[l] == value:
        return l
    elif r < countRegiments + 1 and r + cnt_reg < countRegiments + 1 and   prefix_sum[r+cnt_reg] - prefix_sum[r] == value:
        return r
    return -1

f = open('input.txt')
countRegiments, countIntelligence =  map(int, f.readline().split())
regiments = list(map(int, f.readline().split()))
regiments_set = set(regiments)
if len(regiments_set)!=1:
    prefix_sum = [0]
    summ = 0
    for reg in regiments:
        summ += reg
        prefix_sum.append(summ)
    for i in range(countIntelligence):
        count_regiments, sum_regiments = map(int, f.readline().split())
        l = bin_search(sum_regiments, count_regiments)
        if l == -1:
            print(l)
            continue
        print(l+ 1)
else:
    reg = regiments[0]
    for request in range(countIntelligence):
        count_regiments, sum_people = map(int, f.readline().split())
        if reg*count_regiments != sum_people:
            print(-1)
        else:
            print(1)


