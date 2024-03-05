n = int(input())
lis = list(map(int, input().split()))
lis.sort()
result = 0
for i, t in enumerate(lis[::-1]):
    result += (i+1) * t

print(result)