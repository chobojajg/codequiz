def solution(n):
    answer = ''
    alist = []
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            alist.append("수")
        else:
            alist.append("박")
    answer = "".join(alist)
    
    return answer