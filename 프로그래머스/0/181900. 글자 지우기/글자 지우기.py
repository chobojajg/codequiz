def solution(my_string, indices):
    answer = []
    for i in range(len(my_string)):
        if i not in indices:
            answer.append(my_string[i])
    return ''.join(answer)