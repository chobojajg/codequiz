import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = []

for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 이동했을 때 1인 경우 + 벽에 안 부딛혔을 때
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

    return maze[n - 1][m - 1]


print(bfs(0, 0))