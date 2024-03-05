def solution(array, height):
    count = 0
    for i in array:
        if i > height:
            count += 1
    return count
# def solution(array, height):
#     answer = 0
#     array.sort()
    
#     for i in range(len(array)):
#         if array[i] > height:
#             answer = len(array) - i
#             return answer
#     return 0