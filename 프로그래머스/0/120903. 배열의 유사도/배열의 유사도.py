def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer
#     answer = 0
    
#     for i in s1:
#         for j in s2:
#             if i == j:
#                 answer += 1
    
#     return answer