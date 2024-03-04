def solution(s):
    answer = ''
    slist = list(s)
    slist.sort(reverse = True)
    
    answer = "".join(slist)
    
    return answer