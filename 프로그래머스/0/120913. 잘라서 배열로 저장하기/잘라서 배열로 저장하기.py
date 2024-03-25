def solution(my_str, n):
    answer = []
    index = 0
    
    while(True):
        if index + n >= len(my_str):
            answer.append(my_str[index:])
            break
        answer.append(my_str[index:index + n])
        index += n
    
    return answer