def solution(num):
    answer = 0
    count = 0
    
    while(num != 1):
        if num % 2 == 0:
            num = num / 2
        elif num % 2 == 1:
            num = num * 3 + 1
        count = count + 1
        if count == 500:
            count = -1
            break
    
    answer = count
            
    return answer