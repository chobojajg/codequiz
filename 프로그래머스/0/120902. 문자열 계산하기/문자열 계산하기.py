def solution(my_string):
#     answer = 0
#     lis = my_string.split()
#     num = []
#     piv = []
    
#     for i in lis:
#         if i.isdigit():
#             num.append(i)
#         else:
#             piv.append(i)
            
#     answer += int(num[0])
#     for i in range(len(piv)):
#         if piv[i] == "+":
#             answer += int(num[i+1])
#         elif piv[i] == "-":
#             answer -= int(num[i+1])
#     return answer
    
    return eval(my_string)