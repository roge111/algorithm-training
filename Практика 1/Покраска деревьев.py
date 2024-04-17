vasyaNumberTree, vasyaCountTree = map(int, input().split())
mashaNumberTree, mashaCountTree= map(int, input().split())


print(2 * (vasyaCountTree + mashaCountTree + 1) - max(0, min(vasyaNumberTree + vasyaCountTree, mashaNumberTree + mashaCountTree) - max(vasyaNumberTree - vasyaCountTree, mashaNumberTree - mashaCountTree) + 1))

# elif vasyaNumberTree != mashaNumberTree:
#     # elif abs(vasyaNumberTree + vasyaCountTree) - mashaNumberTree - mashaCountTree >= 0 or vasyaNumberTree + vasyaCountTree <= mashaNumberTree - mashaCountTree:
#     #     slog_1 = max(abs(vasyaNumberTree - vasyaCountTree), abs(mashaNumberTree - mashaCountTree))
#     #     slog_2 = (max(vasyaNumberTree + vasyaCountTree,mashaNumberTree + mashaCountTree))
#     #     countResult  += max(abs(vasyaNumberTree - vasyaCountTree), abs(mashaNumberTree - mashaCountTree)) + (max(vasyaNumberTree + vasyaCountTree,mashaNumberTree + mashaCountTree)) + 1
#     elif vasyaNumberTree < mashaNumberTree and (vasyaNumberTree + vasyaCountTree >= mashaNumberTree - mashaCountTree):
#         #r = 0
#         countResult  = max(abs(vasyaNumberTree - vasyaCountTree), abs(mashaNumberTree - mashaCountTree)) + (max(vasyaNumberTree + vasyaCountTree,mashaNumberTree + mashaCountTree)) + 1
#     elelif mashaNumberTree < vasyaNumberTree and (mashaNumberTree + mashaCountTree >= vasyaNumberTree - vasyaCountTree):
#         #r = 0
#         countResult  = max(abs(vasyaNumberTree - vasyaCountTree), abs(mashaNumberTree - mashaCountTree)) + (max(vasyaNumberTree + vasyaCountTree,mashaNumberTree + mashaCountTree)) + 1

#     else:
#         #r = 0
#         countResult = vasyaCountTree*2 + 1 + mashaCountTree*2 + 1
# elelif vasyaNumberTree == mashaNumberTree:
#     countResult = max(vasyaCountTree, mashaCountTree)*2+1
# print(countResult)
# 2 * (vasyaCountTree + mashaCountTree + 1) - max({0, min({vasyaNumberTree + vasyaCountTree, mashaNumberTree + mashaCountTree}) - max({vasyaNumberTree - vasyaCountTree, mashaNumberTree - mashaCountTree}) + 1})