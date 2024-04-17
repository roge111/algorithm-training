# def chek(k: int):
#     summ = (k*(k+1)*(k+2))//6
#     return summ, (k*(k+1)//2)

# def bin_search(n: int):
#     l, r = 1, n//2 + 1
#     while l < r -1:
#         mid = (l+r)//2
#         summ, cnt= chek(mid)
#         if summ + cnt -1 > n:
#             r = mid
#         else:
#             l = mid
#     if r == 1:
#         return r
#     return l

# countCells = int(input())
# if countCells == 0:
#     print(0)
# else:
#     print(bin_search(countCells))

def can_place_ships(k):
    summ = (k*(k+1)*(k+2))//6
    return summ + (k*(k+1)//2) -1


def binary_search(n):
    if n == 0:
        return 0
    left = 1
    # if n > 10**15:
    #     left = 181709
    # if n > 10**17:
    #     left = 800000
    right = 2*10**6
    while left < right-1:
        mid = (left + right) // 2
        if can_place_ships(mid) <= n:
            left = mid
        else:
            right = mid
    return left


n = int(input())
result = binary_search(n)
print(result)
