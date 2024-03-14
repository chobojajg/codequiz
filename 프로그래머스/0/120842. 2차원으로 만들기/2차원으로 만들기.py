def solution(num_list, n):
    answer = []
    index = 0
    while index < len(num_list):
        answer.append(num_list[index:index+n])
        index += n
    return answer