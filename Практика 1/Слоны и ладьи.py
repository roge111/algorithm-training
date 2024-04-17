n, m = 8, 8
desk = []
bool_desk = []
for i in range(n):
    desk.append(input())
    bool_desk.append([True, True, True, True, True, True, True, True])
cords = []
for i in range(n):
    for j in range(m):
        if desk[i][j] == 'R':
            bool_desk[i][j] = False
            i_d = i-1
        
            while i_d >=0:
                if desk[i_d][j] == 'R' or desk[i_d][j] == 'B':
                    break
                if bool_desk[i_d][j]:
                    bool_desk[i_d][j] = False
                
                i_d -=1
            i_d = i+1
            while i_d <= 7:
                if desk[i_d][j] == 'R' or desk[i_d][j] == 'B':
                    break
                if bool_desk[i_d][j]:
                    bool_desk[i_d][j] = False
                
                i_d += 1
            j_d = j - 1
            while j_d >= 0:
                if desk[i][j_d] == 'R' or desk[i][j_d] == 'B':
                    break
                if bool_desk[i][j_d]:
                    bool_desk[i][j_d] = False
                
                j_d -=1
            j_d = j+1
            while j_d <= 7:
                if desk[i][j_d] == 'R' or desk[i][j_d] == 'B':
                    break
                if bool_desk[i][j_d]:
                    bool_desk[i][j_d] = False
                
                j_d += 1
        elif desk[i][j] == 'B':
            bool_desk[i][j] = False

            i_d = i-1
            j_d = j+1
            while i_d >=0 and j_d <= 7:
                if desk[i_d][j_d] == 'R' or desk[i_d][j_d] == 'B':
                    break
                if bool_desk[i_d][j_d]:
                    bool_desk[i_d][j_d] = False
                i_d -= 1
                j_d += 1

            i_d = i + 1
            j_d = j - 1
            while j_d >=0 and i_d <= 7:
                if desk[i_d][j_d] == 'R' or desk[i_d][j_d] == 'B':
                    break
                if bool_desk[i_d][j_d]:
                    bool_desk[i_d][j_d] = False
                j_d -= 1
                i_d += 1

            i_d = i-1
            j_d = j-1
            while i_d >=0 and j_d >= 0:
                if desk[i_d][j_d] == 'R' or desk[i_d][j_d] == 'B':
                    break
                if bool_desk[i_d][j_d]:
                    bool_desk[i_d][j_d] = False
                i_d -= 1
                j_d -= 1

            i_d = i + 1
            j_d = j + 1
            while i_d <= 7 and j_d <= 7:
                if desk[i_d][j_d] == 'R' or desk[i_d][j_d] == 'B':
                    break
                if bool_desk[i_d][j_d]:
                    bool_desk[i_d][j_d] = False
                i_d += 1
                j_d += 1

             
        
result = 0
for i in range(n):
    result += bool_desk[i].count(True)
print(result)

