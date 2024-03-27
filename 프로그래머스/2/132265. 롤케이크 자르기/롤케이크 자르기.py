def solution(topping):
    answer = 0
    left = {}
    right = {}
    for i in topping:
        if i not in right:
            right[i] = 0
        right[i] += 1
    for i in topping:
        if i not in left:
            left[i] = 0
        left[i] += 1
        right[i] -= 1
        if right[i] == 0:
            del right[i]
        lln = len(left)
        rln = len(right)
        if lln == rln:
            answer += 1
        elif lln > rln:
            break
    return answer

# 7 - 6번보다 더줄임, 시간초과
# def solution(topping):
#     answer = 0
#     left = []
#     right = {}
#     for i in topping:
#         if i not in right:
#             right[i] = 0
#         right[i] += 1
#     for i in topping:
#         left.append(i)
#         right[i] -= 1
#         if right[i] == 0:
#             del right[i]
#         lln = len(set(left))
#         rln = len(right)
#         if lln == rln:
#             answer += 1
#         elif lln > rln:
#             break
#     return answer

# 6 - 5번보다 더 줄였지만 시간초과
# def solution(topping):
#     answer = 0
#     bother = []
#     for i in range(len(topping)):
#         bother.append(topping.pop(0))
#         b = len(set(bother))
#         t = len(set(topping))
#         if b > t:
#             break
#         if b == t:
#             answer += 1
#     return answer

# 5 - 2번 사용해서 4번보다 더욱 시간을 줄였으나 여전히 시간초과
# def solution(topping):
#     answer = 0
#     bother = []
#     for i in range(len(topping)):
#         bother.append(topping.pop(0))
#         if len(set(bother)) == len(set(topping)):
#             answer += 1
#     return answer

# 4 - 1번에서 굳이 리스트로 안만들고 set 그대로 사용해서 시간을 줄였으나 시간초과
# def solution(topping):
#     answer = 0
#     for i in range(len(topping)):
#         if len(set(topping[:i])) == len(set(topping[i:])):
#             answer += 1
#     return answer

# 3 - 0번 마저 만들었는데 실패, 너무 깊어서 런타임 에러등 문제 발생
# answer = 0
# def solution(topping):
#     visit = [False] * (len(topping))
#     cutpos = len(topping) // 2
#     def dfs(cut):
#         global answer
#         visit[cut] = True
#         a = len(list(set(topping[:cut])))
#         b = len(list(set(topping[cut:])))
#         if a == b:
#             answer += 1
#         if a < b and not visit[cut + 1] and 0 < cut < len(topping):
#             dfs(cut + 1)
#         elif a > b and not visit[cut - 1] and 0 < cut < len(topping):
#             dfs(cut - 1)
#         elif a == b and 0 < cut < len(topping):
#             if not visit[cut + 1]:
#                 dfs(cut + 1)
#             elif not visit[cut - 1]:
#                 dfs(cut - 1)
#         return
#     dfs(cutpos)
#     return answer

# 2 - 시간 초과
# def solution(topping):
#     answer = 0
#     bother = []
#     for i in range(len(topping)):
#         bother.append(topping.pop(0))
#         if len(list(set(bother))) == len(list(set(topping))):
#             answer += 1
#     return answer

# 1 - 시간 초과
# def solution(topping):
#     answer = 0
#     for i in range(len(topping)):
#         if len(list(set(topping[:i]))) == len(list(set(topping[i:]))):
#             answer += 1
#     return answer

# 0 - 만들다 말았음
# def solution(topping):
#     answer = -1
#     a = 0
#     b = len(topping)
#     cut = b // 2
#     cutlist = []
#     while a != b:
#         a = len(list(set(topping[:cut])))
#         b = len(list(set(topping[cut:])))
#         if cut in cutlist:
#             break
#     return answer