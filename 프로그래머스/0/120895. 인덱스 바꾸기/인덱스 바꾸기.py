def solution(my_string, num1, num2):
    answer = ''
    st = ''
    lis = list(my_string)
    
    st = lis[num1]
    lis[num1] = lis[num2]
    lis[num2] = st
    
    answer = "".join(lis)
    
    return answer