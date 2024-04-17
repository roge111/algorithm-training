countSectors = int(input())
valuesSectors = list(map(int, input().split()))
speedStart, speedEnd, resistance = map(int, input().split())
maximum = max(valuesSectors)
maxValue = 0
l = len(valuesSectors)
if speedEnd >= resistance:
    for speedNow in range(speedStart, speedEnd+1, resistance):
        countSectorsBe = speedNow//resistance
        
        if countSectorsBe > countSectors-1:
            countSectorsBe = countSectorsBe%countSectors
        if speedNow%resistance == 0:
            countSectorsBe -= 1
        
        if speedNow > resistance:
            if countSectorsBe > 0:
                value1 = valuesSectors[countSectorsBe]
                value2 = valuesSectors[- (countSectorsBe)]
            else:
                value1 = valuesSectors[countSectorsBe]
                value2 = valuesSectors[- (countSectorsBe) ]
            if value1 > maxValue: 
                maxValue = value1
            if value2 > maxValue:
                maxValue = value2
            
        else:
            if valuesSectors[0] > maxValue:
                maxValue = valuesSectors[0]
        if maxValue == maximum:
            break
else:
    maxValue = valuesSectors[0]
print(maxValue)