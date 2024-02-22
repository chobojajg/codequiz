def solution(num_list):
    sumnum = 0
    multnum = 1
    sumnum = sum(num_list)
    sumnum = sumnum * sumnum
    for i in num_list:
        multnum = multnum * i
    if sumnum > multnum:
        return 1
    else :
        return 0