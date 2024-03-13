import sys
from collections import deque
n, m, start = map(int, sys.stdin.readline().split())
dic = [[]]
for i in range(1, n + 1):
    dic.append([])
    dic[i] = []
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
for i in range(1, len(dic)):
    dic[i].sort()
dfs_v = [0] * (n + 1)
bfs_v = dfs_v[:]


def dfs(graph, start, visit):
    visit[start] = start
    print(start, end=' ')

    for i in graph[start]:
        if visit[i] == 0:
            dfs(graph, i, visit)


def bfs(graph, start, visit):
    queue = deque([start])
    visit[start] = start

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if visit[i] == 0:
                queue.append(i)
                visit[i] = i


dfs(dic, start, dfs_v)
print('')
bfs(dic, start, bfs_v)