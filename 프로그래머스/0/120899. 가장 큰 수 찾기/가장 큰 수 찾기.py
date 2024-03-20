def solution(array):
    return [max(array), array.index(max(array))]


    # answer = [0, 0]
    # num = array[0]
    # for i in range(len(array)):
    #     if num < array[i]:
    #         num = array[i]
    #         answer[0] = num
    #         answer[1] = i