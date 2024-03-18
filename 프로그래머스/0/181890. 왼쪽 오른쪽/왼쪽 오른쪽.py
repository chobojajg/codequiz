def solution(str_list):
    answer = []
    l_index = -1
    r_index = -1
    if 'l' in str_list:
        l_index = str_list.index('l')
    if 'r' in str_list:
        r_index = str_list.index('r')
    if l_index == -1 and r_index == -1:
        return answer
    elif l_index == -1:
        return str_list[r_index + 1:]
    elif r_index == -1:
        return str_list[:l_index]
    else:
        if l_index < r_index:
            return str_list[:l_index]
        else:
            return str_list[r_index + 1:]