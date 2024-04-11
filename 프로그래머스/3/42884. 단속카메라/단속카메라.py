def solution(routes):
    answer = 1
    routes.sort(key=lambda x:min(x))
    c = 40000
    for i, o in routes:
        if c < i:
            answer += 1
            c = o
        c = min(c, o)
    return answer
    

# def solution(routes):
#     check = []
#     routes.sort(key=lambda x:min(x))
#     c = 40000
#     for i, o in routes:
#         if len(check) == 0:
#             check.append([i, o])
#             continue
#         if c < i:
#             check.append([i, o])
#             c = o
#         c = min(c, o)
#     return len(check)

# def solution(routes):
#     check = []
#     routes.sort(key=lambda x:min(x))
#     for i in routes:
#         c = 0
#         if not len(check):
#             check.append(i)
#             continue
#         for j in check:
#             if min(i) <= max(j):
#                 j[j.index(min(j))] = min(i)
#                 c = 1
#                 break
#         if not c:
#             check.append(i)
#     return len(check)