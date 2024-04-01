def solution(arr):
    arr.remove(min(arr))
    if not len(arr):
        arr.append(-1)
    return arr

# def solution(arr):
#     answer = []
#     arrlen = len(arr)
#     num = arr[0]
    
#     for i in range(len(arr)):
#         if arr[i] <= num:
#             num = arr[i]
    
#     #while minnum in arr:
#     arr.remove(num)
    
#     answer = arr
    
#     if len(answer) == 0:
#         answer = [-1]
    
#     return answer