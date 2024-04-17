count = int(input())
data = list(map(int, input().split()))
hash_map = {}
for el in data:
    if el in hash_map:
        hash_map[el] += 1
    else:
        hash_map[el] = 1
count_save = 0
for key in hash_map:
    cur_save = hash_map[key]
    if  (key+1) in hash_map:
        cur_save += hash_map[key+1]
    if cur_save > count_save:
        count_save = cur_save
print(count - count_save)
