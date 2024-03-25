def solution(X, Y):
    answer = ''
    li = []
    check = "9"
    while int(check) >= 0:
        for i in range(min(X.count(check), Y.count(check))):
            li.append(check)
        check = str(int(check) - 1)
        
    if len(li) == 0:
        return "-1"
    if li[0] == "0":
        return "0"
    answer = "".join(li)
    return answer
    
    # answer = ''
    # li = []
    # lix = list(X)
    # liy = list(Y)
    # for i in lix:
    #     if i in liy:
    #         liy.remove(i)
    #         li.append(i)
    # if len(li) == 0:
    #     return "-1"
    # li.sort(reverse=True)
    # answer = "".join(li)
    # answer = str(int(answer))
    # return answer