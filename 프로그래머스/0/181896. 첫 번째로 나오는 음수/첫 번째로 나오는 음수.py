def solution(num_list):
    cnt = 0
    for i in num_list:
        if i < 0:
            return cnt
        cnt += 1
    return -1

# def solution(num_list):
#     for i in num_list:
#         if i < 0:
#             return num_list.index(i)
#     return -1