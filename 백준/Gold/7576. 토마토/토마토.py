import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))
cnt = 0
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(pos_list, cnt):
    queue = deque()
    for i in pos_list:
        queue.append((i[0], i[1]))

    while True:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 상하좌우 이동했을 때 1인 경우 + 벽에 안 부딛혔을 때
                if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                    queue.append((nx, ny))
                    tomato[nx][ny] = 1
        if len(queue) == 0:
            break
        cnt += 1

    return cnt


pos = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            pos.append([i, j])
cnt = bfs(pos, cnt)
ct = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            ct += 1
if ct != 0:
    print(-1)
else:
    print(cnt)