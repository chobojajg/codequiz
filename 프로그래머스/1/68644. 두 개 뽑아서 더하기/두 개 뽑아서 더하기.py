def solution(numbers):
    answer = []
    numbers.sort()
    ilis = numbers[:-1]
    
    for i in range(len(ilis)):
        jlis = numbers[i + 1:]
        for j in range(len(jlis)):
            answer.append(ilis[i]+jlis[j])
    
    answer = list(set(answer))
    answer.sort()
    return answer