# 4         cnt 4
# 3 1       cnt 3 1
# 2 2       cnt 2 2
# 2 1 1     cnt 2 1 1
# 1 1 1 1   cnt 1 1 1 1
def solution(a, b, c, d):
    dice = [a, b, c, d]
    answer = 0
    check = []
    cnt = []
    for i in range(4):
        if dice[i] in check:
            cnt[check.index(dice[i])] += 1
        else:
            check.append(dice[i])
            cnt.append(1)
    if 4 in cnt:
        return 1111 * a
    elif 3 in cnt:
        return (10 * check[cnt.index(3)] + check[cnt.index(1)]) ** 2
    elif 2 in cnt:
        if 1 in cnt:
            check.pop(cnt.index(2))
            return check[0] * check[1]
        else:
            return (check[0] + check[1]) * abs(check[0] - check[1])
    else:
        return min(check)
    
    return answer