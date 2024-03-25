import operator
def solution(files):
    answer = []
    dic = {}
    result = []
    
    for i in range(len(files)):
        head = ''
        num = ''
        tail = ''
        headli = []
        numli = []
        tailli = []
        files[i]
        lis = list(files[i].lower())
        for j in lis:
            if j.isdigit() and num == '':
                if head == '':
                    head = "".join(headli)
                numli.append(j)
            else :
                if len(numli) == 0:
                    headli.append(j)
                else:
                    if num == '':
                        num = "".join(numli)
                        break
                    tailli.append(j)
        if num == '':
            num = "".join(numli)
        tail = "".join(tailli)
        dic[files[i]] = ([head, int(num)])
    result = sorted(dic.items(), key=operator.itemgetter(1))
    
    for i in result:
        answer.append(i[0])
    
    return answer