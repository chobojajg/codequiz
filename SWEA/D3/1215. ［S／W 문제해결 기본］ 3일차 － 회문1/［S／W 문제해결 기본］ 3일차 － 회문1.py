def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


T = 10
for test_case in range(1, T + 1):
    word_len = int(input())
    board = []
    result = 0
    for i in range(8):
        board.append(list(input()))
    rot_board = rotate_90(board)
    for i in range(8):
        for j in range(word_len, 9):
            if j == 8:
                if board[i][j - word_len:] == board[i][j - word_len:][::-1]:
                    result += 1
                if rot_board[i][j - word_len:] == rot_board[i][j - word_len:][::-1]:
                    result += 1
            else:
                if board[i][j - word_len:j] == board[i][j - word_len:j][::-1]:
                    result += 1
                if rot_board[i][j - word_len:j] == rot_board[i][j - word_len:j][::-1]:
                    result += 1

    print(f'#{test_case} {result}')
