countPeople = int(input())
hash_map = {}
for i in range(countPeople):
    countSongs = int(input())
    songs = input().split()
    for song in songs:
        if song in hash_map:
            hash_map[song] += 1
        else:
            hash_map[song] = 1
result = []
cnt = 0
for song in hash_map:
    if hash_map[song] == countPeople:
        cnt += 1
        result.append(song)
print(cnt)
print(' '.join(sorted(result)))

