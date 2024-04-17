
def count_lines (words: list, width: int):
    cnt = 0
    summ_line = 0
    for el in words:
        if summ_line + el <= width:
            summ_line += el + 1
        else:
            cnt += 1
            summ_line = el+1
    cnt += 1
    return cnt

def bin_search(widthRoll: int, max_1: int, max_2: int, cntWords_1: int, cntWords_2: int):
    l, r =max_1-1, widthRoll - max_2 + 1
    res = max(cntWords_1, cntWords_2)
    while l < r - 1:
        mid = (l+r)//2
        countRows_1 = count_lines(wordsFirstPart, mid)
        countRows_2 = count_lines(wordsSecondPart, widthRoll - mid)
        res = min(res, max(countRows_1, countRows_2))
        if countRows_1 == 0 or countRows_1 > countRows_2:
            l = mid
        else:
            r = mid
    

    return res


widthRoll, countWords_1, countWords_2 = map(int, input().split())
wordsFirstPart = list(map(int, input().split()))
wordsSecondPart = list(map(int, input().split()))
maximum_1, maximum_2 = max(wordsFirstPart), max(wordsSecondPart)
print(bin_search(widthRoll, maximum_1, maximum_2, countWords_1, countWords_2))
