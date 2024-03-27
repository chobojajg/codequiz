def solution(m, n, puddles):
    answer = 0
    road = [[0]*m for i in range(n)]
    road[0][0] = 1
    for i in puddles:
        road[i[1]-1][i[0]-1] = -1
    print(road)
    for i in range(1, n):
        if [1, i+1] in puddles:
            break
        else:
            road[i][0] = 1
    for i in range(1, m):
        if [i+1, 1] in puddles:
            break
        else:
            road[0][i] = 1
    print(road)
    for i in range(1, n):
        for j in range(1, m):
            if road[i][j] != -1:
                if road[i-1][j] == -1 and road[i][j-1] == -1:
                    continue
                elif road[i-1][j] == -1:
                    road[i][j] = road[i][j-1]
                elif road[i][j-1] == -1:
                    road[i][j] = road[i-1][j]
                else:
                    road[i][j] = road[i-1][j] + road[i][j-1]
    print(road)
    return road[n-1][m-1] % 1000000007

# 1 - bfs 사용했으나 런타임 에러, 시간초과, 틀림 3종세트
# from collections import deque
# def solution(m, n, puddles):
#     road = []
#     for i in range(n):
#         road.append([])
#         for j in range(m):
#             road[i].append(0)
#     for i in puddles:
#         road[i[0]][i[1]] = -1
#     dx = [1, 0]
#     dy = [0, 1]

#     def bfs(x, y):
#         queue = deque()
#         queue.append((x, y))

#         while queue:
#             x, y = queue.popleft()

#             for i in range(2):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx < n and ny < m and road[nx][ny] != -1:
#                     queue.append((nx, ny))
#                     road[nx][ny] += 1

#         return road[n - 1][m - 1]

#     answer = bfs(0, 0)
#     return answer % 1000000007