def solution(common):
    answer = 0
    a = common[1] - common[0]
    b = common[2] - common[1]
    
    if a == b:
        if a == 0:
            return common[-1]
        return common[-1] + a
    else:
        return common[-1] * (b / a)