paper = []
for i in range(100):
    paper.append([])
    for j in range(100):
        paper[i].append(0)

lis = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            paper[i][j] = 1
result = 0
for i in paper:
    result += sum(i)

print(result)