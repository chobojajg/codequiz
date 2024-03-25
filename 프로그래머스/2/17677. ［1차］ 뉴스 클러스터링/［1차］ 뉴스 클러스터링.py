def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    lis1 = []
    lis2 = []
    inter = []
    union = []
    
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            lis1.append(str1[i:i+2])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            lis2.append(str2[i:i+2])

    union = lis1 + lis2
    for i in lis1:
        if i in lis2:
            lis2.pop(lis2.index(i))
            inter.append(i)
    for i in inter:
        union.remove(i)
    
    if len(union) == 0:
        if len(inter) == 0:
            answer = 65536
        else:
            answer = 0
    else:
        answer = int((len(inter) / len(union)) * 65536)
    
    return answer