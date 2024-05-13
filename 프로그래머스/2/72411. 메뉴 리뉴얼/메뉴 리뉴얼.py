from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        data = []
        for order in orders:
            comb = combinations(order, i)
            for j in comb:
                data.append(''.join(sorted(j)))
        dic = Counter(data).most_common()
        if len(dic):
            for m, c in dic:
                if c > 1 and c == dic[0][1]:
                    answer.append(m)
    answer = sorted(answer)
    return answer

# 1 - 그냥 틀림(테스트케이스)
# def checkmenu(base, check):
#     menu = list(check)
#     result = []
#     for e in base:
#         lis = []
#         for j in e:
#             if j in e:
#                 lis.append(j)
#         if len(lis) > 1:
#             result.append(''.join(sorted(lis)))
#     result = list(set(result))
#     return result
# def solution(orders, course):
#     answer = []
#     result = []
#     for i in orders:
#         answer += checkmenu(orders, i)
#     answer = list(set(answer))
#     for i in answer:
#         if len(i) in course:
#             result.append(i)
#     result = sorted(result)
#     return result