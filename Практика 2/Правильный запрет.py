countOfRaces, countOfClass = map(int, input().split())
hash_map = []



for i in range(1, countOfRaces+1):    
    hash_map.append(list(map(int, input().split()))  )
min_res = 10**10
res_race, res_class = 0, 0
for index in range(countOfRaces):
   
    for i in range(countOfClass):
        
        
        classNumber = i + 1
        maximum = 0
        for row in range(countOfRaces):
            
            if row == index:
                continue
            for colomn in range(countOfClass):
                if colomn+1 == classNumber:
                    continue
                el = hash_map[row][colomn]
                if el > maximum:
                    maximum = el
                
        if maximum < min_res:
            min_res = maximum
            res_class = classNumber
            res_race = index+1
print(res_race, res_class)

# countOfRaces, countOfClass = map(int, input().split())
# hash_map = {}



# for i in range(1, countOfRaces+1):    
#     hash_map[i] = list(map(int, input().split()))  
# min_res = 10**10
# res_race, res_class = 0, 0
# for key in hash_map:
   
#     for i in range(countOfClass):
        
        
#         classNumber = i + 1
#         maximum = 0
#         for row in range(1, countOfRaces+1):
            
#             if row == key:
#                 continue
#             for colomn in range(countOfClass):
#                 if colomn+1 == classNumber:
#                     continue
#                 el = hash_map[row][colomn]
#                 if el > maximum:
#                     maximum = el
                
#         if maximum < min_res:
#             min_res = maximum
#             res_class = classNumber
#             res_race = key
# print(res_race, res_class)