def solution(players, callings):
    runner = {}
    rank = {}
    answer = []
    for i in range(1, len(players) + 1):
        runner[i] = players[i - 1]
        rank[players[i - 1]] = i
    for i in callings:
        idx = rank[i]
        rank[runner[idx]], rank[runner[idx - 1]] = rank[runner[idx - 1]], rank[runner[idx]]
        runner[idx], runner[idx - 1] = runner[idx - 1], runner[idx]
    for i in range(1, len(runner) + 1):
        answer.append(runner[i])
    return answer
    

# 1번 시도 - 시간초과 9, 10, 11, 12, 13
# def solution(players, callings):
#     for i in callings:
#         idx = players.index(i)
#         players[idx - 1], players[idx] = players[idx], players[idx - 1]
#     return players