#65 <= A <= 90
#97 <= a <= 122

def solution(s, n):
    answer = ''
    lis = list(s)
    num = 0
    
    for i in range(len(lis)):
        if lis[i] == " ":
            continue
        num = ord(lis[i]) + n
        if ord(lis[i]) <= 90:
            if 90 < num:
                num -= 26
        elif ord(lis[i]) <= 122:
            if 122 < num:
                num -= 26
        lis[i] = chr(num)
    
    answer = "".join(lis)
    
    return answer

# def solution(s, n):
#     answer = ''
#     lis = list(s)
#     #n = n % 26
#     num = 0
    
#     for i in range(len(lis)):
#         if lis[i] == " ":
#             continue
#         num = ord(lis[i]) + n
#         if ord(lis[i]) <= 90:
#             if 90 < num:
#                 num -= 26
#         elif ord(lis[i]) <= 122:
#             if 122 < num:
#                 num -= 26
#         lis[i] = chr(num)
    
#     # for i in range(len(lis)):
#     #     if lis[i] == " ":
#     #         continue
#     #     num = ord(lis[i]) + n
#     #     if num < 65:
#     #         num += 26
#     #     elif 90 < num and num < 97:
#     #         if ord(lis[i]) <= 90:
#     #             num -= 26
#     #         elif 97 <= ord(lis[i]):
#     #             num += 26
#     #     elif 122 <= num:
#     #         num -= 26
#     #     lis[i] = chr(num)
    
#     answer = "".join(lis)
    
#     return answer