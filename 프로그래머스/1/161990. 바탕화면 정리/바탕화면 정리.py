def solution(wallpaper):
    answer = [100, 100, 0, 0]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if i < answer[0]:
                    answer[0] = i
                if i > answer[2]:
                    answer[2] = i
                if j < answer[1]:
                    answer[1] = j
                if j > answer[3]:
                    answer[3] = j
    answer[2] += 1
    answer[3] += 1
    return answer