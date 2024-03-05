def solution(my_string, letter):
    answer = ''
    lis = list(my_string)
    
    lis = [i for i in lis if i != letter]
    
    answer = "".join(lis)
    
    return answer