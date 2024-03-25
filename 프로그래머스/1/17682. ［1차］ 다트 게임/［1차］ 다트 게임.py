def solution(dartResult):
    answer = 0
    lis = list(dartResult)
    stack = []
    for i in range(len(lis)):
        if lis[i].isdigit():
            if lis[i] == "0" and i != 0:
                if lis[i - 1] == "1":
                    stack.pop()
                    stack.append(10)
                else:
                    stack.append(int(lis[i]))
            else:
                stack.append(int(lis[i]))
        elif lis[i] == "S":
            stack[-1] = stack[-1] ** 1
        elif lis[i] == "D":
            stack[-1] = stack[-1] ** 2
        elif lis[i] == "T":
            stack[-1] = stack[-1] ** 3
        elif lis[i] == "*":
                stack[-1] *= 2
                if len(stack) > 1:
                    stack[-2] *= 2
        elif lis[i] == "#":
            stack[-1] = stack[-1] * -1
    answer = sum(stack)
            
    return answer