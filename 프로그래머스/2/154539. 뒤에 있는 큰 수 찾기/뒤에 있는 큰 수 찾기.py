def solution(numbers):
    answer = []
    stack = []
    for i in reversed(numbers):
        if len(stack) == 0:
            stack.append(i)
            answer.append(-1)
            continue
        while len(stack) > 0:
            if stack[-1] <= i:
                stack.pop()
            else:
                break
        stack.append(i)
        if len(stack) == 1:
            answer.append(-1)
        else:
            answer.append(stack[-2])
    return answer[::-1]

# 4 - 1번보다 빠르지만 시간초과
# def solution(numbers):
#     ln = len(numbers)
#     answer = [-1 for i in range(ln)]
#     for i in range(ln):
#         for j in range(i, ln):
#             if numbers[i] < numbers[j]:
#                 answer[i] = numbers[j]
#                 break
#     return answer

# 3 - 시간 초과 1번보다 느리고 2번보다 빠름
# def solution(numbers):
#     answer = []
#     ln = len(numbers)
#     for i in range(ln):
#         for j in range(ln):
#             if numbers[0] < numbers[j]:
#                 answer.append(numbers[j])
#                 numbers.pop(0)
#                 break
#             elif numbers[0] == max(numbers):
#                 answer.append(-1)
#                 numbers.pop(0)
#                 break
#     return answer   

# 2 - 시간 초과, 1번보다 느림
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i, len(numbers)):
#             if numbers[i] < numbers[j]:
#                 answer.append(numbers[j])
#                 break
#             elif numbers[i] == max(numbers[i:]):
#                 answer.append(-1)
#                 break
    
#     return answer

# 1 - 시간 초과
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i, len(numbers)):
#             if numbers[i] < numbers[j]:
#                 answer.append(numbers[j])
#                 break
#         if i + 1 > len(answer):
#             answer.append(-1)
        
#     return answer