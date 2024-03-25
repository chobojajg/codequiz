#row 는 가로
#column 은 세로
#row > column

def solution(brown, yellow):
    answer = []
    alcar = brown + yellow
    row = alcar
    column = 0
    lis = []
    
    while(row > column):
        li = []
        if alcar % row == 0:
            column = int(alcar / row)
            li.append(row)
            li.append(column)
            lis.append(li)
        row -= 1
    
    for i in range(len(lis)):
        if (sum(lis[i]) * 2) - 4 == brown:
            if (lis[i][0] - 2) * (lis[i][1] - 2) == yellow:
                answer = lis[i]
    
    return answer