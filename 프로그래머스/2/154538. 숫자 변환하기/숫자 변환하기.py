from collections import deque
def solution(x, y, n):
    answer = []
    dic = {}
    check = 0
    
    que = deque([(x, 0)])
    
    while que:
        v, c = que.popleft()
        
        if v >= y:
            if v == y:
                answer.append(c)
                check = 1
        else:
            if v*3 <= y and v*3 not in dic:
                que.append((v*3, c+1))
                dic[v*3] = c+1
            if v*2 <= y and v*2 not in dic:
                que.append((v*2, c+1))
                dic[v*2] = c+1
            if v+n <= y and v+n not in dic:
                que.append((v+n, c+1))
                dic[v+n] = c+1
    if check:
        return min(answer)
    else:
        return -1
        

# 5 - 압도적으로 시간 줄임, 여전히 1개만 시간초과
# import sys
# sys.setrecursionlimit(10**7)
# cnt = 10000000
# def solution(x, y, n):
#     global cnt
#     def dfs(x,y,n, c):
#         global cnt
#         if x > y:
#             return
#         if x == y and cnt > c:
#             cnt = c
#             return
#         if cnt > c:
#             if y % 3 == 0:
#                 dfs(x, y // 3, n, c + 1)
#         if cnt > c:
#             if y % 2 == 0:
#                 dfs(x, y // 2, n, c + 1)
#         if cnt > c:
#             dfs(x, y - n, n, c + 1)
#         return
#     dfs(x, y, n, 0)
#     if cnt == 10000000:
#         return -1
#     return cnt

# 4 - 시간초과, 1개만 남음
# import sys
# sys.setrecursionlimit(10**7)
# def solution(x, y, n):
#     cnt = [10000000]
#     def dfs(x,y,n, c):
#         if x > y:
#             return
#         if x == y:
#             cnt.append(c)
#             return
#         if min(cnt) > c:
#             if y % 3 == 0:
#                 dfs(x, y // 3, n, c + 1)
#             if y % 2 == 0:
#                 dfs(x, y // 2, n, c + 1)
#             dfs(x, y - n, n, c + 1)
#     dfs(x, y, n, 0)
#     cnt.remove(10000000)
#     if not len(cnt):
#         return -1
#     return min(cnt)

# 3 - 뎁스 문제 해결
# import sys
# sys.setrecursionlimit(10**7)
# def solution(x, y, n):
#     cnt = []
#     def dfs(x,y,n, c):
#         if x > y:
#             return
#         if x == y:
#             cnt.append(c)
#             return
#         dfs(x + n, y, n, c + 1)
#         dfs(x * 2, y, n, c + 1)
#         dfs(x * 3, y, n, c + 1)
#     dfs(x, y, n, 0)
#     if not len(cnt):
#         return -1
#     return min(cnt)

# 2 - 시간초과, 런타임 에러
# import sys
# sys.setrecursionlimit(10**6)
# def solution(x, y, n):
#     cnt = []
#     def dfs(x,y,n, c):
#         if x > y:
#             return
#         if x == y:
#             cnt.append(c)
#             return
#         dfs(x + n, y, n, c + 1)
#         dfs(x * 2, y, n, c + 1)
#         dfs(x * 3, y, n, c + 1)
#     dfs(x, y, n, 0)
#     if not len(cnt):
#         return -1
#     return min(cnt)

# 1 - 최소값 비교 없음
# import sys
# sys.setrecursionlimit(10**6)
# answer = 0
# def solution(x, y, n):
#     global answer
#     def dfs(x,y,n):
#         global answer
#         if x > y:
#             return
#         if x == y:
#             answer += 1
#             return
#         dfs(x + n, y, n)
#         dfs(x * 2, y, n)
#         dfs(x * 3, y, n)
#     dfs(x, y, n)
#     if not answer:
#         answer = -1
#     return answer