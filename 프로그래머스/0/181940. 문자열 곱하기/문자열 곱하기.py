def solution(my_string, k):
    answer = ''
    for i in range(k):
        answer += my_string
    return answer
    # lis = []
    # for i in range(k):
    #     lis.append(my_string)
    # answer = ''.join(lis)
    # return answer