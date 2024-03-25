def solution(n, works):
    answer = 0
    if sum(works) < n:
        return answer
    works.sort(reverse=True)
    stand = int((sum(works) - n) / len(works)) + 1
    num = 0
    if works[-1] >= stand:
        for i in range(len(works)):
            num += works[i] - stand
            works[i] = stand
        n -= num
    else:
        num = 0
        ii = 0
        for i in range(1, len(works)):
            ii = i
            num += (works[i - 1] - works[i]) * i
            if num >= n:
                stand = int((sum(works[:i]) - n) / len(works[:i])) + 1
                break
        num = 0
        for i in range(len(works[:ii])):
            num += works[i] - stand
            works[i] = stand
        n -= num
    count = 0
    while n > 0:
        if count == len(works):
            count -= len(works)
        works[count] -= 1
        n -= 1
        count += 1
    for i in works:
        answer += i ** 2
    return answer
    

#     answer = 0
#     works.sort(reverse=True)
#     if sum(works) <= n:
#         return 0
#     stand = int((sum(works) - n) / len(works)) + 1
#     rangenum = len(works)
#     if works[-1] < stand:
#         num = 0
#         for i in range(1, len(works)):
#             num = num + ((works[i - 1] - works[i]) * i)
#             if n < num:
#                 stand = int((sum(works[:i]) - n) / len(works[:i])) + 1
#                 rangenum = len(works[:i])
#                 break
#         for j in range(rangenum):
#             works[j] = stand
#             n -= (works[j] - (stand))
        
#     for i in range(rangenum):
#         while works[i] > stand:
#             if n == 0:
#                 break
#             works[i] -= 1
#             n -= 1
#     if n != 0:
#         for i in range(len(works)):
#             works[i] -= 1
#             n -= 1
#             if n == 0:
#                 break
#     for i in works:
#         answer += i ** 2
    
#     return answer