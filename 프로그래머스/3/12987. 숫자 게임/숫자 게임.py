import heapq
def solution(A, B):
    answer = 0
    a = [-i for i in A]
    b = [-i for i in B]
    heapq.heapify(a)
    heapq.heapify(b)
    while b and a:
        an = heapq.heappop(a)
        bn = heapq.heappop(b)
        if -an < -bn:
            answer += 1
        else:
            heapq.heappush(b, bn)
    return answer
    
# 2 - 시간초과
# def solution(A, B):
#     answer = 0
#     B.sort()
#     for i in A:
#         c = 0
#         ln = len(B)
#         while c < len(B):
#             if B[c] > i:
#                 if B[c] > i:
#                     answer += 1
#                 B.pop(c)
#                 break
#             else:
#                 c += 1
#         if ln == len(B):
#             B.pop(0)
#     return answer

# 1 - 17번 틀림, 효율성 시간초과
# def solution(A, B):
#     answer = 0
#     B.sort()
#     for i in A:
#         c = 0
#         ln = len(B)
#         while c < len(B):
#             if B[c] > i:
#                 if B[c] >= i:
#                     answer += 1
#                 B.pop(c)
#                 break
#             else:
#                 c += 1
#         if ln == len(B):
#             B.pop(0)
#     return answer