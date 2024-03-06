def solution(numbers, direction):
    answer = []
    num = 0
    
    if direction == "right":
        answer.append(numbers[-1])
        del numbers[-1]
        answer = answer + numbers
    elif direction == "left":
        num = numbers[0]
        del numbers[0]
        answer = numbers[:]
        answer.append(num)
    return answer