def solution(N, stages):
    answer = []
    lis = {}
    player = len(stages)
    for i in range(1, N + 1):
        if player < 1:
            lis[i] = 0
            continue
        count = 0
        for j in stages:
            if j == i:
                count += 1
        lis[i] = count / player
        player -= count
    
    lis = sorted(lis.items(), reverse = True, key=lambda item: item[1])
    
    for key, value in lis:
        answer.append(key)
    
    return answer