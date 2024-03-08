n = int(input())
num_list = list(map(int, input().split()))
op = list(map(int, input().split()))
max_num = -1000000000
min_num = 1000000000
result = [max_num, min_num]

def cal_num(cnt, max_cnt, sum_num, op, num_list):
    global result
    if cnt == max_cnt:
        if sum_num > result[0]:
            result[0] = sum_num
        if sum_num < result[1]:
            result[1] = sum_num
        return

    if op[0]:
        op[0] -= 1
        cal_num(cnt + 1, max_cnt, sum_num + num_list[cnt], op, num_list)
        op[0] += 1
    if op[1]:
        op[1] -= 1
        cal_num(cnt + 1, max_cnt, sum_num - num_list[cnt], op, num_list)
        op[1] += 1
    if op[2]:
        op[2] -= 1
        cal_num(cnt + 1, max_cnt, sum_num * num_list[cnt], op, num_list)
        op[2] += 1
    if op[3]:
        op[3] -= 1
        cal_num(cnt + 1, max_cnt, int(sum_num / num_list[cnt]), op, num_list)
        op[3] += 1


cal_num(1, n, num_list[0], op, num_list)
print(result[0])
print(result[1])