def solution(arr):
    answer = [0, 0]
    ln = len(arr)
    def quad(x, y, l):
        s = arr[x][y]
        for i in range(x, x+l):
            for j in range(y, y+l):
                if arr[i][j] != s:
                    l = l//2
                    quad(x,y,l)
                    quad(x,y+l,l)
                    quad(x+l,y,l)
                    quad(x+l,y+l,l)
                    return
        answer[s] += 1
    quad(0,0,ln)
    return answer