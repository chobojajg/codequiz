def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    for bal in babbling:
        n = -1
        while True:
            if len(bal) == 0:
                answer += 1
                break
                
            if bal[:3] == can[0] and n != 0:
                bal = bal[3:]
                n = 0
            elif bal[:2] == can[1] and n != 1:
                bal = bal[2:]
                n = 1
            elif bal[:3] == can[2] and n != 2:
                bal = bal[3:]
                n = 2
            elif bal[:2] == can[3] and n != 3:
                bal = bal[2:]
                n = 3
            else:
                break
    return answer
        

# 2 번째 시도
# answer = 0
# can = ['aya', 'ye', 'woo', 'ma']
# n = -1

# def babblcheck(babbl, num = -1):
#     global answer
#     global n
#     for i in range(4):
#         if can[i] in babbl and i != n:
#             print(babbl, answer, n)
#             n = i
#             babbl = babbl[:babbl.index(can[i])] + babbl[babbl.index(can[i]) + len(can[i]):]
#             if len(babbl) == 0:
#                 answer += 1
#                 return
#             else:
#                 babblcheck(babbl, n)


# def solution(babbling):
#     for babbl in babbling:
#         babblcheck(babbl)

#     return answer

# 1 번째 시도
# def solution(babbling):
#     answer = 0
#     can = ['aya', 'ye', 'woo', 'ma']
#     for i in babbling:
#         for j in can:
#             if j in i:
#                 i = i.replace(j,'')
#             if len(i) == 0:
#                 answer += 1
#                 break
#     return answer