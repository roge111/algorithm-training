

def check(k: int): # номер диагонали 
    n_1, n_2 = 0, 0
    if k%2 == 0:
        n_1 = (k-1) * k//2 + + 1
        n_2 = k*(k+1)//2
    else:
        n_2 = (k-1) * k//2 + + 1
        n_1 = k*(k+1)//2
    
    return n_1, n_2

def bin_search(value:int):
    l, r = 1, value
    n_1, n_2 = 1, 1
    while l < r - 1:
        mid = (l+r)//2
        n_1, n_2 = check(mid)
        if n_2 > n_1:
            if value > n_2:
                l = mid
            elif value < n_1:
                r = mid
            else:
                l= mid
                break    
        else:
            if value > n_1:
                l = mid
            elif value < n_2:
                r = mid
            else:
                l = mid
                break
    x = abs(value - n_1)
    return l - x, 1 +  x
    
k = int(input())
if k <= 2:
    i, j = k, 1
else:
    i, j = bin_search(k)
print(i, end='/')
print(j)
# k = int(input())
# n = (-1 + (1**2 + 8*k)**0.5)/2
# print(n)