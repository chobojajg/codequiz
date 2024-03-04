def solution(s):
    answer = ''
    lis = list(s)
    slis = []
    wordlis = []
    for i in range(len(lis)):
        if lis[i] != " ":
            slis.append(lis[i])
            if i == len(lis) - 1:
                wordlis.append("".join(slis))
                slis.clear()
            continue
        
        wordlis.append("".join(slis))
        slis.clear()
        wordlis.append(" ")
    
    for i in range(len(wordlis)):
        if wordlis[i] == " ":
            continue
        strlis = list(wordlis[i])
        for j in range(len(strlis)):
            if j % 2 == 0:
                strlis[j] = strlis[j].upper()
            else:
                strlis[j] = strlis[j].lower()
        wordlis[i] = "".join(strlis)
    
    answer = "".join(wordlis)
    
    return answer