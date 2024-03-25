def solution(s):
    return int(s)
        

# def solution(s):
#     answer = 0
    
#     sarr = list(s)
#     lista = []
#     signlist = []
#     numlist = []
#     resultlist = []
    
#     if sarr[0] == "-":
#         signlist.append(-1)
#     else:
#         signlist.append(1)
    
#     for i in range(len(sarr)):
#         print(sarr[i])
#         if sarr[i] == "+":
#             if i == 0:
#                 continue
#             numlist.append(int("".join(lista)))
#             signlist.append(1)
#             lista = []
            
#         elif sarr[i] == "-":
#             if i == 0:
#                 continue
#             numlist.append(int("".join(lista)))
#             signlist.append(-1)
#             lista = []
            
#         else:
#             lista.append(sarr[i])
            
#         if i + 1 == len(sarr):
#             numlist.append(int("".join(lista)))
    
#     for i in range(len(numlist)):
#         resultlist.append(numlist[i] * signlist[i])
    
#     answer = sum(resultlist)
    
#     return answer