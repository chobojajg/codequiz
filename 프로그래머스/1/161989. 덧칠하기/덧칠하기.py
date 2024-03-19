def solution(n, m, section):
    answer = 1
    check = -1
    for i in range(len(section)):
        if check == -1:
            check = section[i]
        if check + m - 1 >= section[i]:
            continue
        else:
            check = section[i]
            answer += 1
    return answer
        
    
    
# def solution(n, m, section):
#     answer = 0
#     wall = []
#     roller = []
#     for i in range(m):
#         roller.append(1)
#     for i in range(n):
#         if (i + 1) in section:
#             wall.append(0)
#         else:
#             wall.append(1)
#     for i, b in enumerate(wall):
#         if b == 0:
#             wall[i:i + m] = roller
#             answer += 1

#     return answer