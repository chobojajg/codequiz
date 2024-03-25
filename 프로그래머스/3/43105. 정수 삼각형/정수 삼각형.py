memo = {0:0}
def solution(triangle):
    lis = []
    for i in triangle:
        lis.clear()
        for j in range(len(i)):
            if j == 0:
                lis.append(memo[j] + i[j])
            else:
                if j == len(i) - 1:
                    lis.append(memo[j - 1] + i[j])
                else:
                    if memo[j] + i[j] >= memo[j - 1] + i[j]:
                        lis.append(memo[j] + i[j])
                    else:
                        lis.append(memo[j - 1] + i[j])
        for k in range(len(lis)):
            memo[k] = lis[k]
    answer = max(memo.values())
    return answer