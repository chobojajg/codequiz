def solution(my_string):
    answer = ''
    li = list(my_string)
    removeset = {"a", "e", "i", "o", "u"}
    
    li = [i for i in li if i not in removeset]
    
    answer = "".join(li)
    
    return answer