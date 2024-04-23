def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(plays)):
        if genres[i] not in dic:
            dic[genres[i]] = [0, []]
        dic[genres[i]][0] += plays[i]
        dic[genres[i]][1].append([plays[i], i])
    check = sorted(dic.items(), key=lambda item: item[1][0], reverse=True)
    for key, value in check:
        value[1].sort(key=lambda x: (-x[0], x[1]))
        for i in range(2):
            answer.append(value[1][i][1])
            if len(value[1]) < 2:
                break
    return answer

# 3 - 실패, 2번보다 1개 더 성공
# def solution(genres, plays):
#     answer = []
#     dic = {}
#     for i in range(len(plays)):
#         if genres[i] not in dic:
#             dic[genres[i]] = [0, []]
#         dic[genres[i]][0] += plays[i]
#         dic[genres[i]][1].append([plays[i], i])
#     check = sorted(dic.items(), key=lambda item: item[0], reverse=True)
#     for key, value in check:
#         value[1].sort(key=lambda x: (-x[0], x[1]))
#         for i in range(2):
#             answer.append(value[1][i][1])
#             if len(value[1]) < 2:
#                 break
#     return answer

# 2 - 실패
# def solution(genres, plays):
#     answer = []
#     dic = {}
#     for i in range(len(plays)):
#         if genres[i] not in dic:
#             dic[genres[i]] = [0, []]
#         dic[genres[i]][0] += plays[i]
#         dic[genres[i]][1].append([plays[i], i])
#     check = sorted(dic.items(), key=lambda item: item[0], reverse=True)
#     for key, value in check:
#         value[1].sort(reverse=True)
#         for i in range(2):
#             answer.append(value[1][i][1])
#             if len(value[1]) < 2:
#                 break
#     return answer

# 1 - 실패, 런타임 에러
# def solution(genres, plays):
#     answer = []
#     dic = {}
#     for i in range(len(plays)):
#         if genres[i] not in dic:
#             dic[genres[i]] = [0, []]
#         dic[genres[i]][0] += plays[i]
#         dic[genres[i]][1].append([plays[i], i])
#     check = sorted(dic.items(), key=lambda item: item[0], reverse=True)
#     for key, value in check:
#         value[1].sort(reverse=True)
#         for i in range(2):
#             answer.append(value[1][i][1])
#     return answer