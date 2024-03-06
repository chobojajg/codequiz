big_num = []
for i in range(9):
    line_num = list(map(int, input().split()))
    big_num.append([i, line_num.index(max(line_num)), max(line_num)])

big_num.sort(key = lambda x : x[2])
print(big_num[-1][2])
print(big_num[-1][0] + 1, big_num[-1][1] + 1)