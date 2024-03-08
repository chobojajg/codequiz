from itertools import combinations
l, c = map(int, input().split())
lst = list(input().split())
lst.sort()
all_list = list(combinations(lst, l))
con_list = ['a', 'e', 'i', 'o', 'u']
for i in range(len(all_list)):
    con = 0
    gather = 0
    for j in all_list[i]:
        if j in con_list:
            con += 1
        else:
            gather += 1
    if con >= 1 and gather >= 2:
        print(''.join(all_list[i]))