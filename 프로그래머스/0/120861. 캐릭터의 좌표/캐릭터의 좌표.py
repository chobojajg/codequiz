def solution(keyinput, board):
    answer = [0, 0]
    upboard = (board[1] - 1) / 2
    downboard = -1 * upboard
    rightboard = (board[0] - 1) / 2
    leftboard = -1 * rightboard
    for i in keyinput:
        if i == "up":
            answer[1] += 1
            if answer[1] > upboard:
                answer[1] -= 1
        elif i == "down":
            answer[1] -= 1
            if answer[1] < downboard:
                answer[1] += 1
        elif i == "right":
            answer[0] += 1
            if answer[0] > rightboard:
                answer[0] -= 1
        elif i == "left":
            answer[0] -= 1
            if answer[0] < leftboard:
                answer[0] += 1
    return answer