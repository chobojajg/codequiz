def solution(my_string, overwrite_string, s):
    ms = list(my_string)
    os = list(overwrite_string)
    
    for i in range(len(os)):
        ms[i+s] = os[i]
    
    answer = ''.join(ms)
    return answer