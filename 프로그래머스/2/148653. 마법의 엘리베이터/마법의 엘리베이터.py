def solution(storey):
    answer = 0
    lis = list(str(storey))[::-1]
    lis = list(map(int, lis))
    ln = len(lis)
    for i in range(ln):
        if lis[i] == 5:
            answer += 5
            if i != ln - 1:
                if lis[i+1] >= 5:
                    lis[i+1] += 1
        elif lis[i] > 5:
            answer += (10 - lis[i])
            if i == ln - 1:
                answer += 1
            else:
                lis[i+1] += 1
        else:
            answer += lis[i]
            lis[i] = 0
    return answer

# 1 - 실패, 로직이 잘못됬음, 반례 - 999
# def solution(storey):
#     dic = {"6":"5", "7":"4","8":"3","9":"2"}
#     lis = list(str(storey))
#     for i in range(len(lis)):
#         if lis[i] in dic:
#             lis[i] = dic[lis[i]]
#     answer = sum(list(map(int, lis)))
#     return answer