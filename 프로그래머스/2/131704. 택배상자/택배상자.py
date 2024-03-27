def solution(order):
    answer = 0
    main = []
    sub = []
    order = order[::-1]
    for i in range(len(order), -1, -1):
        main.append(i)
    while len(order):
        if len(main) and len(sub):
            if order[-1] == main[-1]:
                order.pop()
                main.pop()
                answer += 1
            else:
                if sub[-1] == order[-1]:
                    order.pop()
                    sub.pop()
                    answer += 1
                else:
                    while order[-1] != main[-1]:
                        sub.append(main.pop())
                        if not len(main):
                            break
                        if main[-1] == order[-1]:
                            order.pop()
                            main.pop()
                            answer += 1
                            break
        elif not len(main) and len(sub):
            if sub[-1] == order[-1]:
                order.pop()
                sub.pop()
                answer += 1
            else:
                break
        elif len(main) and not len(sub):
            if order[-1] == main[-1]:
                order.pop()
                main.pop()
                answer += 1
            else:
                while order[-1] != main[-1]:
                    sub.append(main.pop())
                    if not len(main):
                        break
                    if main[-1] == order[-1]:
                        order.pop()
                        main.pop()
                        answer += 1
                        break
    return answer
    

# 3 - 시간 초과
# def solution(order):
#     answer = 0
#     main = []
#     sub = []
#     order = order[::-1]
#     for i in range(len(order), -1, -1):
#         main.append(i)
#     while len(order):
#         if len(main) and len(sub):
#             if order[-1] in main:
#                 if order[-1] == main[-1]:
#                     order.pop()
#                     main.pop()
#                     answer += 1
#                 else:
#                     while order[-1] != main[-1]:
#                         sub.append(main.pop())
#             elif order[-1] in sub:
#                 if sub[-1] == order[-1]:
#                     order.pop()
#                     sub.pop()
#                     answer += 1
#                 else:
#                     break
#         elif not len(main) and len(sub):
#             if sub[-1] == order[-1]:
#                 order.pop()
#                 sub.pop()
#                 answer += 1
#             else:
#                 break
#         elif len(main) and not len(sub):
#             if order[-1] in main:
#                 if order[-1] == main[-1]:
#                     order.pop()
#                     main.pop()
#                     answer += 1
#                 else:
#                     while order[-1] != main[-1]:
#                         sub.append(main.pop())
#             elif order[-1] in sub:
#                 if sub[-1] == order[-1]:
#                     order.pop()
#                     sub.pop()
#                     answer += 1
#                 else:
#                     break
#     return answer

# 2 - 시간 초과
# def solution(order):
#     answer = 0
#     main = []
#     sub = []
#     for i in range(1, len(order) + 1):
#         sub.append(i)
#     while sub[-1] != order[0]:
#         main.append(sub.pop())
#     while len(order):
#         if len(sub) != 0:
#             if sub[-1] == order[0]:
#                 sub.pop()
#                 order.pop(0)
#                 answer += 1
#         if len(main) != 0:
#             if main[-1] == order[0]:
#                 main.pop()
#                 order.pop(0)
#                 answer += 1
#         if len(order) > 0:
#             if order[0] in main:
#                 while main[-1] != order[0]:
#                     sub.append(main.pop())
#         if len(main) == 0 and len(sub) != 0:
#             if sub[-1] != order[0]:
#                 break
#         elif len(sub) == 0 and len(main) != 0:
#             if main[-1] != order[0]:
#                 break
#         elif len(main) != 0 and len(sub) != 0:
#             if sub[-1] != order[0] and main[-1] != order[0]:
#                 break
#         else:
#             break
#     return answer

# 1 - 틀림, 보조 컨테이너가 앞뒤로 움직일 수 있다는걸 간과함 = 중간에 상자 더 추가 가능
# def solution(order):
#     answer = 0
#     main = []
#     sub = []
#     for i in range(1, len(order) + 1):
#         sub.append(i)
#     while sub[-1] != order[0]:
#         main.append(sub.pop())
#     while len(order) > 0:
#         if len(sub) != 0:
#             if sub[-1] == order[0]:
#                 sub.pop()
#                 order.pop(0)
#                 answer += 1
#         if len(main) != 0:
#             if main[-1] == order[0]:
#                 main.pop()
#                 order.pop(0)
#                 answer += 1
#         if order[0] in main:
#                 while sub[-1] != order[0]:
#                     main.append(sub.pop())
            
#         if len(main) == 0 and len(sub) != 0:
#             if sub[-1] != order[0]:
#                 break
#         elif len(sub) == 0 and len(main) != 0:
#             if main[-1] != order[0]:
#                 break
#         elif len(main) != 0 and len(sub) != 0:
#             if sub[-1] != order[0] and main[-1] != order[0]:
#                 break
#         else:
#             break
#     return answer