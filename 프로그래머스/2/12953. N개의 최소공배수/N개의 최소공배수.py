from math import gcd

def solution(arr):
#     answer = 1
#     arr.sort()
    
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[j] % arr[i] == 0:
#                 arr[j] = arr[j] / arr[i]
#         answer *= arr[i]
    
#     answer = int(answer)

    answer = arr[0]
    for i in range(1, len(arr)):
        answer = (answer*arr[i]) // gcd(answer, arr[i])
    
    return answer