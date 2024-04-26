from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    limit = len(queue1)*3
    t1 = sum(queue1)
    t2 = sum(queue2)
    while answer < limit:
        if t1 > t2:
            n = q1.popleft()
            q2.append(n)
            t1 -= n
            t2 += n
        elif t1 < t2:
            n = q2.popleft()
            q1.append(n)
            t1 += n
            t2 -= n
        else:
            break
        answer += 1
    if answer == limit:
        answer = -1
    return answer

# 1 - 1번 실패
# from collections import deque
# def solution(queue1, queue2):
#     answer = 0
#     q1 = deque(queue1)
#     q2 = deque(queue2)
#     limit = len(queue1)*2
#     t1 = sum(queue1)
#     t2 = sum(queue2)
#     while answer < limit:
#         if t1 > t2:
#             n = q1.popleft()
#             q2.append(n)
#             t1 -= n
#             t2 += n
#         elif t1 < t2:
#             n = q2.popleft()
#             q1.append(n)
#             t1 += n
#             t2 -= n
#         else:
#             break
#         answer += 1
#     if answer == limit:
#         answer = -1
#     return answer