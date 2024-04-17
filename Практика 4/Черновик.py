# def chek(s: str):
#     stack = []
#     hash_map = {'(': ')', '[': ']', '{': '}'}
#     for el in s:
#         if el in hash_map:
#             stack.append(el)
#         elif not stack:
#             return False
#         elif hash_map[stack[-1]] == el:
#             stack.pop()
#         else:
#             return False
#     return not stack
# print(chek(input()))
# 8 9 + 1 7 - *

data = input().split()
stack = []
for el in data:
    if el == '+':
        b =stack.pop()
        a = stack.pop()
        stack.append(a+b)

    elif el == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a-b)

    elif el == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a*b)
    else:
        stack.append(int(el))
print(stack[0])