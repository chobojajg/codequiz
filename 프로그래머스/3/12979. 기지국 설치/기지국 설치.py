import math
def solution(n, stations, w):
    answer = 0
    check = 0
    ln = 2*w+1
    for i in stations:
        answer += math.ceil((i-w-1-check)/ln)
        check = i+w
        if check > n:
            check = n
    if check != n:
        answer += math.ceil((n-check)/ln)
    return answer
    
# 3 - 효율성 시간초과    
# import math
# def solution(n, stations, w):
#     answer = 0
#     ln = (2 * w) + 1
#     check = []
#     num = 0
#     result = []
#     for i in stations:
#         for j in range(-w,w+1):
#             if i+j < 1:
#                 continue
#             elif i+j > n:
#                 break
#             check.append(i+j)
#     for i in range(1, n+1):
#         if i in check:
#             if num:
#                 result.append(num)
#                 num = 0
#             continue
#         num += 1
#         if i == n:
#             result.append(num)
#     for i in result:
#         answer += math.ceil(i/ln)
#     return answer

# 2 - 효율성 시간 초과
# def solution(n, stations, w):
#     answer = 0
#     check = [1 for i in range(n)]
#     for i in stations:
#         for j in range(i - 1 - w, i + w):
#             if 0 <= j < n:
#                 check[j] = 0
#     m = w * 2 + 1
#     for i in range(len(check)):
#         if check[i]:
#             for j in range(i, i+m):
#                 if j < n:
#                     check[j] = 0
#             answer += 1
#     return answer

# 1 - 런타임 에러, 실패, 시간초과
# def solution(n, stations, w):
#     answer = 1
#     check = -1
#     section = [i for i in range(1, n+1)]
#     for i in stations:
#         for j in range(i - w, i + w + 1):
#             if 0 < j <= n:
#                 section.remove(j)
#     m = w * 2 + 1
#     for i in range(len(section)):
#         if check == -1:
#             check = section[i]
#         if check + m - 1 >= section[i]:
#             continue
#         else:
#             check = section[i]
#             answer += 1
#     return answer