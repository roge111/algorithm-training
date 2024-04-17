def bin_search_min(value: int, arr: list):
    l, r = -1, len(arr)
    
    while l < r-1:
        m = (l+r)//2
        if arr [m] < value:
            l = m
        else:
            r = m
    if l != -1 and arr[l] >= value:
        return l
    return r
    
def bin_search_max(value: int, arr: list):
    l, r = -1, len(arr)
    while l < r - 1:
        mid = (l+r)//2
        if arr[mid] <= value:
            l = mid
        elif arr[mid] > value:
            r = mid
    if arr[r-1] <= value:
        return r
    return l

count  = int(input())
arr = list(map(int, input().split()))
countRequests = int(input())
arr.sort()
for request in range(countRequests):
    left, right = map(int, input().split())
    l = bin_search_min(left, arr)
    i = l+1
    if l != -1 and l < count and arr[l] <= right:
        r = bin_search_max(right, arr) -1
        print(r - l + 1)
    else:
        print(0)