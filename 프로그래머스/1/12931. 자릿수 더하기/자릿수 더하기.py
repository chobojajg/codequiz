def solution(n):
    arr = list(map(int, str(n)))
    return sum(arr)
    
# def solution(n):
#     strarr = list(str(n))
#     numarr = []
#     for i in range(len(strarr)):
#         numarr.append(int(strarr[i]))
#     return sum(numarr)