def solution(ingredient):
    answer = 0
    burger = [1, 2, 3, 1]
    if len(ingredient) > 3:
        table = [ingredient[0], ingredient[1], ingredient[2]]
        ln = len(ingredient)
        for i in range(3, ln):
            table.append(ingredient[i])
            if ingredient[i] == 1:
                if table[-4:] == burger:
                    table.pop()
                    table.pop()
                    table.pop()
                    table.pop()
                    answer += 1
    return answer

# 5번 시도 - 런타임 에러, 4번보다 시간을 압도적으로 줄임
# def solution(ingredient):
#     answer = 0
#     burger = [1, 2, 3, 1]
#     table = [ingredient[0], ingredient[1], ingredient[2]]
#     ln = len(ingredient)
#     for i in range(3, ln):
#         table.append(ingredient[i])
#         if ingredient[i] == 1:
#             if table[-4:] == burger:
#                 table.pop()
#                 table.pop()
#                 table.pop()
#                 table.pop()
#                 answer += 1
#     return answer

# 4번 시도 - 시간초과 및 런타임 에러, 3번엔 없던 런타임 에러를 제외하면 더 빨라졌음
# def solution(ingredient):
#     answer = 0
#     burger = [1, 2, 3, 1]
#     table = [ingredient[0], ingredient[1], ingredient[2]]
#     ln = len(ingredient)
#     for i in range(3, ln):
#         table.append(ingredient[i])
#         if ingredient[i] == 1:
#             if table[-4:] == burger:
#                 table = table[:-4]
#                 answer += 1
#     return answer

# 3번시도 - 시간초과 2번보나 나음
# def solution(ingredient):
#     answer = 0
#     burger = [1, 2, 3, 1]
#     ln = len(ingredient)
#     for i in range(3, ln):
#         if ingredient[i] == 1:
#             if ingredient[i - 3:i + 1] == burger:
#                 ingredient = [0, 0, 0, 0] + ingredient[:i - 3] + ingredient[i + 1:]
#                 answer += 1
#     return answer

# 2번 시도 - 시간초과
# def solution(ingredient):
#     answer = 0
#     burger = [1, 2, 3, 1]
#     check = 1
#     lst = 0
#     while check:
#         lst = ingredient[:]
#         for i in range(len(ingredient) - 1):
#             if i == len(ingredient) - 2:
#                 check = 0
#             if ingredient[i:i+4] == burger:
#                 ingredient = ingredient[:i] + ingredient[i+4:]
#                 answer += 1
#                 break
#         if ingredient == lst:
#             check = 0
#     return answer 

# 1번 시도
# def solution(ingredient):
#     answer = 0
#     bur = [1, 2, 3, 1]
#     stk = []
#     check = 0
#     for i in ingredient:
#         stk.append(i)
#         if check == 1 and stk[-1] == 2:
#             check = 2
#         elif check == 2 and stk[-1] == 3:
#             check = 3
#         elif check == 3 and stk[-1] == 1:
#             answer += 1
#             check = 0
#             stk.pop()
#             stk.pop()
#             stk.pop()
#             stk.pop()
#             if stk[-1] == 1:
#                 check = 1
#         elif stk[-1] == 1:
#             check = 1
#         else:
#             check = 0
#     return answer