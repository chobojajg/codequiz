def solution(sequence, k):
    answer = [0, 0]
    cnt = []
    if sequence[0] == k:
        print(1)
        return [0, 0]
    elif sequence[-1] == k:
        print(2)
        idx = len(sequence) - 1
        return [idx, idx]
    elif k in sequence:
        print(3)
        idx = sequence.index(k)
        return [idx, idx]
    else:
        num = 0
        for i in range(len(sequence)):
            num += sequence[i]
            answer[1] += 1
            while num > k:
                num -= sequence[answer[0]]
                answer[0] += 1
            if num == k:
                cnt.append([answer[1]-answer[0],[answer[0],answer[1]-1]])
    cnt.sort(key=lambda x: x[0])
    return cnt[0][1]

# 2 - 또 33번만 실패
# def solution(sequence, k):
#     answer = [0, 0]
#     cnt = []
#     if sequence[-1] == k:
#         idx = len(sequence) - 1
#         return [idx, idx]
#     elif sequence[0] == k:
#         return [0, 0]
#     elif k in sequence:
#         idx = sequence.index(k)
#         return [idx, idx]
#     else:
#         num = 0
#         for i in range(len(sequence)):
#             num += sequence[i]
#             answer[1] += 1
#             while num > k:
#                 num -= sequence[answer[0]]
#                 answer[0] += 1
#             if num == k:
#                 cnt.append([answer[1]-answer[0],[answer[0],answer[1]-1]])
#     cnt.sort(key=lambda x: x[0])
#     return cnt[0][1]

# 1 - 33번만 실패
# def solution(sequence, k):
#     answer = [0, 0]
#     cnt = []
#     if sequence[-1] == k:
#         idx = len(sequence) - 1
#         return [idx, idx]
#     else:
#         num = 0
#         for i in range(len(sequence)):
#             num += sequence[i]
#             answer[1] += 1
#             while num > k:
#                 num -= sequence[answer[0]]
#                 answer[0] += 1
#             if num == k:
#                 cnt.append([answer[1]-answer[0],[answer[0],answer[1]-1]])
#     cnt.sort(key=lambda x: x[0])
#     return cnt[0][1]