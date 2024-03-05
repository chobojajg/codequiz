n = int(input())
lis = []
for i in range(n):
    lis.append(list(map(int, input().split())))
lis.sort()
lis.sort(key = lambda x : x[1])

answer = 0
end = 0

for t in lis :
    if t[0] >= end : 
        answer += 1
        end = t[1]

print(answer)