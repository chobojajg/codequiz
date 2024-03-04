def solution(numbers):
    answer = -1
    allnum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in range(len(numbers)):
        allnum.remove(numbers[i])
        
    answer = sum(allnum)
    
    return answer