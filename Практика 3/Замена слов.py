def bin_s(data_clear, word):
    l, r = -1, len(data_clear)
    while l < r-1:
        m = (l+r)//2
        cur_data_clear = data_clear[m]
        if cur_data_clear < word[:len(cur_data_clear)]:
            l = m
        else:
            r = m
    return r


data = sorted(input().split())
message = input().split()
result = []
data_new = []
ptr1, ptr2 = 0, 1
while ptr1 < len(data):
    if ptr2 < len(data) and data[ptr2].startswith(data[ptr1]):
        ptr2 += 1
    else:
        data_new.append(data[ptr1])
        ptr1  = ptr2

for word in message:
    f = True
    inedx = bin_s(data_new, word)
    if  inedx < len(data_new) and word.startswith(data_new[inedx]):
        result.append(data_new[inedx])
    else:
        result.append(word)
        
print(' '.join(result))