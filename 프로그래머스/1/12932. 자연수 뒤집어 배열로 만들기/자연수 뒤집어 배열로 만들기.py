def solution(n):
    answer = []
    arr = list(map(int, str(n)))
    for i in range(len(arr) - 1, -1, -1):
        answer.append(arr[i])
    return answer

# def solution(n):
#     answer = []
#     arrstr = list(str(n))
    
#     for i in range(len(arrstr)):
#         answer.append(int(arrstr[len(arrstr)-i-1]))
#     return answer