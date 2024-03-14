def solution(s):
    answer = 0
    before = []
    lis = s.split()
    for i in lis:
        if i == "Z":
            if len(before) == 0:
                before.append(0)
            before.pop()
        else:
            before.append(int(i))
    answer = sum(before)
    return answer