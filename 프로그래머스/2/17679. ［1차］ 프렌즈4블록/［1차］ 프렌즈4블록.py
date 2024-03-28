def rotate_90(m):
    N = len(m)
    M = len(m[0])
    ret = [[0] * N for _ in range(M)]

    for r in range(N):
        for c in range(M):
            ret[c][N-1-r] = m[r][c]
    return ret

def rotate_90_r(m):
    N = len(m)
    M = len(m[0])
    ret = [[0] * N for _ in range(M)]

    for r in range(N):
        for c in range(M):
            ret[M-1-c][r] = m[r][c]
    return ret

def solution(m, n, board):
    answer = 0
    check = 1
    while check:
        cboard = []
        for i in range(m):
            cboard.append([])
            for j in range(n):
                cboard[i].append(True)
        check = 0
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '0' and board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                    cboard[i][j] = False
                    cboard[i+1][j] = False
                    cboard[i][j+1] = False
                    cboard[i+1][j+1] = False
                    check = 1
        if check:
            board = rotate_90(board)
            cboard = rotate_90(cboard)
            for i in range(n-1, -1, -1):
                for j in range(m-1, -1, -1):
                    if not cboard[i][j]:
                        board[i][j] = '0'
                        board[i].append(board[i].pop(j))
            board = rotate_90_r(board)
    for i in range(m):
        s = ''.join(board[i])
        answer += s.count('0')
    return answer