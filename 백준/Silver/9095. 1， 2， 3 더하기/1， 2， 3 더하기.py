import sys
lst = [1, 2, 3]


def check_num(num, goal):
    global cnt
    if num == goal:
        cnt += 1
        return

    for i in lst:
        if num < goal:
            check_num(num + i, goal)
        if num > goal:
            return


n = int(sys.stdin.readline())
for _ in range(n):
    a = int(sys.stdin.readline())
    cnt = 0
    sum_num = 0
    check_num(sum_num, a)
    print(cnt)