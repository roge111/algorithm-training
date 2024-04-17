n, k = map(int, input().split())
data = list(map(int, input().split()))
hash_map = {}
f = False
for i, el in enumerate(data):
    if el in hash_map:
        if i - hash_map[el] <= k:
            f = True
            break
        else:
            hash_map[el] = i
    else:
        hash_map[el] = i
if f:
    print('YES')
else:
    print('NO')