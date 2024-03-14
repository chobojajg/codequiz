def solution(n, slicer, num_list):
    answer = []
    if n == 1:
        answer = num_list[:slicer[1] + 1]
    elif n == 2:
        answer = num_list[slicer[0]:]
    elif n == 3:
        answer = num_list[slicer[0]:slicer[1] + 1]
    elif n == 4:
        num_list = num_list[slicer[0]:slicer[1] + 1]
        for i in range(len(num_list)):
            if i % slicer[2] == 0:
                answer.append(num_list[i])
    return answer