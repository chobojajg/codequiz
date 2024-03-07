# def solution(n):
#     answer = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             answer += 1
#     return answer

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if n // i <= i:
                answer *= 2
                if n // i == i:
                    answer += 1
                break
            answer += 1
            
    return answer