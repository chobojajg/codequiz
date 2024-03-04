def solution(sizes):
    answer = 0
    row = []
    column = []
    
    for i in range(len(sizes)):
        sizes[i].sort()
        row.append(sizes[i][0])
        column.append(sizes[i][1])
    
    answer = max(row) * max(column)
    
    return answer