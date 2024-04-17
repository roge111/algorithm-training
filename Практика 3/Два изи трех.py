hash_map = {}
for i in range(3):
    countInt = int(input())
    data = set(map(int, input().split()))
    for el in data:
        if el in hash_map:
            hash_map[el] += 1
        else:
            hash_map[el] = 1
hash_map_2 = sorted(hash_map)
result = []
for el in hash_map_2:
    if hash_map[el] >=2:
        result.append(str(el))
print(' '.join(result))
