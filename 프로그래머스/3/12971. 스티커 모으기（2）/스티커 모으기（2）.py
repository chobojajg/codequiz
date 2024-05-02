def solution(sticker):
    answer = 0
    ln = len(sticker)
    if ln == 1:
        return sticker[0]
    s1 = [0] + sticker[:-1]
    s2 = [0] + sticker[1:]
    for i in range(2, ln):
        s1[i] = max(s1[i-1], s1[i] + s1[i-2])
        s2[i] = max(s2[i-1], s2[i] + s2[i-2])
    answer = max(s1[-1], s2[-1])
    return answer

# 1 - 전혀 틀린 방식
# def solution(sticker):
#     result = [0, 0]
#     for i in range(len(sticker)):
#         if i % 2 == 0:
#             if i == len(sticker) - 1:
#                 break
#             result[0] += sticker[i]
#         else:
#             result[1] += sticker[i]
#     answer = max(result)
#     return answer