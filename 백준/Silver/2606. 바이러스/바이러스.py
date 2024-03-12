com = int(input())
link = int(input())
dic = {}
result = 0
for i in range(1, com + 1):
    dic[i] = []
for i in range(link):
    com1, com2 = map(int, input().split())
    dic[com1].append(com2)
    dic[com2].append(com1)


def dfs_dic(dic, start, v = []):
    v.append(start)
    for i in dic[start]:
        if i not in v:
            dfs_dic(dic, i, v)
    return v
print(len(dfs_dic(dic, 1)) - 1)