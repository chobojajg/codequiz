def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 1:
                try:
                    if board[i - 1][j - 1] == 1 and i - 1 >= 0 and j - 1 >= 0:
                        board[i][j] = 2
                except:
                    pass
                try:
                    if board[i - 1][j] == 1 and i - 1 >= 0:
                        board[i][j] = 2
                except:
                    pass
                try:
                    if board[i - 1][j + 1] == 1 and i - 1 >= 0:
                        board[i][j] = 2
                except:
                    pass
                try:
                    if board[i][j - 1] == 1 and j - 1 >= 0:
                        board[i][j] = 2
                except:
                    pass
                try:
                    if board[i][j + 1] == 1:
                        board[i][j] = 2
                except:
                    pass
                try:
                    if board[i + 1][j - 1] == 1 and j - 1 >= 0:
                        board[i][j] = 2
                except:
                    pass
                try:
                    if board[i + 1][j] == 1:
                        board[i][j] = 2
                except:
                    pass
                try:
                    if board[i + 1][j + 1] == 1:
                        board[i][j] = 2
                except:
                    pass
    for i in board:
        answer += i.count(0)
    return answer