def solution(number, k):
    answer = ''
    stk = []
    knum = k
    for e in number:
        while k > 0 and stk and stk[-1] < e:
            stk.pop()
            k -= 1
        stk.append(e)
    if len(stk) > len(number) - knum:
        stk.remove(min(stk))
    answer = ''.join(stk)
    return answer

# 3 - 시간초과, 실패
# def solution(number, k):
#     answer = ''
#     lis = list(number)
#     cnt = 0
#     while k>0 and cnt<len(lis)-1:
#         if lis[cnt] < lis[cnt+1]:
#             lis.pop(cnt)
#             k -= 1
#             if cnt:
#                 cnt -= 2
#             else:
#                 cnt -= 1
#         cnt += 1
#     answer = ''.join(lis)
#     return answer