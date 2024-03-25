def solution(str1, str2):
    answer = []
    for i in range(len(str1)):
        answer.append(str1[i])
        answer.append(str2[i])
    return ''.join(answer)

# def solution(str1, str2):
#     num = len(str1)+len(str2)
#     lis = []
#     answer = ''
#     for i in range(num):
#         if i%2 == 0:
#             lis.append(str1[i//2])
#         else:
#             lis.append(str2[i//2])
#     answer = ''.join(lis)
#     return answer