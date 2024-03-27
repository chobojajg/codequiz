def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max([e for x, e in enumerate(land[i-1]) if x != j])
    return max(land[len(land) - 1])

# 1 - 시간 초과
# import sys
# sys.setrecursionlimit(1000001)
# def solution(land):
#     answer = 0
#     lst = []
#     def dfs(v, s, cnt = 0):
#         s += land[cnt][v]
#         cnt += 1
#         if cnt == len(land):
#             if len(lst) == 0:
#                 lst.append(s)
#             elif s > max(lst):
#                     lst.append(s)
#             return
#         for i in range(4):
#             if i != v:
#                 dfs(i, s, cnt)

#     for i in range(4):
#         dfs(i, answer)
#     return max(lst)