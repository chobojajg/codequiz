def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


T = int(input())
for test_case in range(1, T + 1):
    page_len, word_len = map(int, input().split())
    result = 0
    page = []
    for i in range(page_len):
        page.append(list(map(int, input().split())))
    ret_page = rotate_90(page)

    for i in range(page_len):
        pcnt = 0
        rpcnt = 0
        for j in range(page_len):
            if page[i][j] == 1:
                pcnt += 1
            else:
                if pcnt == word_len:
                    result += 1
                pcnt = 0

            if ret_page[i][j] == 1:
                rpcnt += 1
            else:
                if rpcnt == word_len:
                    result += 1
                rpcnt = 0

            if j + 1 == page_len:
                if pcnt == word_len:
                    result += 1
                if rpcnt == word_len:
                    result += 1

    print(f'#{test_case} {result}')