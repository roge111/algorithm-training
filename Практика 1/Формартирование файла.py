def format(n):
    cnt  = 0
    while n != 0:
        if n >= 4:
            cnt += n//4
            n = n - 4*cnt
        if n != 0:
            if n%4 == 0:
                n -= 4
                cnt += 1
            elif n%4 == 1:
                n-=1
                cnt += 1 
            elif n%4== 2:
                n -= 2
                cnt += 2 # 2*space
            else:
                n -= 3
                cnt += 2
    return cnt

cnt_string = int(input())
result = 0
for i in range(cnt_string):
    result += format(int(input()))
print(result)