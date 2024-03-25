def changebitandonenumcount(n):
    zero = {"0"}
    lis = []
    n = format(n,'b')
    lis = list(n)
    lis = [i for i in lis if i not in zero]
    return len(lis)

def solution(n):
    answer = n
    count = 0
    need = 0
    count = changebitandonenumcount(n)
    
    while(count != need):
        answer = answer + 1
        need = changebitandonenumcount(answer)
    
    return answer