def solution(n, computers):
    def dfs(v):
        visit[v] = True
        for i in range(n):
            if not visit[i] and computers[v][i]:
                dfs(i)
    answer = 0
    visit = [False] * (n)
    for i in range(n):
        if not visit[i]:
            dfs(i)
            answer += 1
    return answer

# 1번 - 그냥 틀림
# def solution(n, computers):
#     answer = 0
#     com = computers[:]
#     remove_set = {0}
#     for i in range(n):
#         for j in range(i + 1, n):
#             if j == i:
#                 continue
#             if computers[i][j] == 1:
#                 com[j] = 0
#     for i in range(-len(com), 0):
#         n = abs(i) - 1
#         if com[n] == 0:
#             com.pop(n)
#     answer = len(com)
#     return answer