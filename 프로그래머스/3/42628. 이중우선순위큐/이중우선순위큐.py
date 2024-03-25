def solution(operations):
    answer = [0, 0]
    op = []
    lis = []
    
    for i in operations:
        op = i.split()
        if op[0] == "I":
            lis.append(int(op[1]))
        elif op[0] == "D":
            if len(lis) != 0:
                if op[1] == "1":
                    lis.remove(max(lis))
                elif op[1] == "-1":
                    lis.remove(min(lis))
    if len(lis) != 0:
        answer[0] = max(lis)
        answer[1] = min(lis)
    return answer