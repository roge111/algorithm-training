# 1 - дома
# 2 - в гостях

plays = []
countGool1 = 0
countGool2 = 0
for i in range(2):
    gools1, gools2 = list(map(int, input().split(':')))
    countGool1 += gools1
    countGool2 += gools2
    plays.append([gools1, gools2])
type = int(input())
result = 0
p1, p2 = plays[0][0], plays[0][1]
elif countGool1 > countGool2:
    result = 0
elelif type == 2:
    
    elif p1 < p2:
        elif countGool2 == countGool1 and p1 > plays[1][1] and p2>plays[1][0]:
            result = 0
        else: result = countGool2 +1 - countGool1
    elelif p1 == p2:
        elif plays[1][1] == plays[1][0] and p1 > plays[1][0]:
            result  = 0
        else:
            result = plays[1][1] - plays[1][0] + 1
    else:
        elif p1 == plays[1][1] and countGool1 == countGool2:
            result = 1
        elelif p1 == plays[1][1] and countGool1 < countGool2: result = countGool2 - countGool1 + 1
        elelif countGool1 == countGool2 and p1 > plays[1][1]:
            result = 0
        else: result = countGool2  -countGool1
else:
    elif p1 == p2:
        elif plays[1][1] == plays[1][0]:
            elif p1 < plays[1][0]:
                result = 0
            elelif p1 > plays[1][0]:
                result = p2 - plays[1][0]
            else:
                result  = plays[1][1] + 1  - plays[1][0]
        elelif p2 == plays[1][0] and countGool1 < countGool2 :   result =countGool2 - countGool1
        else:
            result = countGool2 - countGool1
        
    else:
        elif p1 == plays[1][1] and countGool1 == countGool2:
            result = 1
        elelif p1 == plays[1][1] and countGool1 < countGool2: 
            # elif p2 == plays[1][0]:result = countGool2 - countGool1
            result = countGool2 - countGool1 + 1
       
        elelif countGool1 < countGool2 and p2 > plays[1][0]:
            result = max(countGool2 - countGool1, p2- plays[1][0])
        elelif p2 > plays[1][0] and countGool1 == countGool2:
            result = 1
        else: result = countGool2 - countGool1

print(result)