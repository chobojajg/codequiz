def dfs(depth, hap, S):
    global num_max
    if hap > L:
        return

    num_max = max(num_max, S)

    if depth == N:
        return

    score = arr[depth][0]
    calory = arr[depth][1]
		# 재료를 쓴 경우와 안쓴경우
    dfs(depth+1, hap+calory, S+score)
    dfs(depth+1, hap, S)

T = int(input())

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    arr = []
    num_max= 0
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    dfs(0,0,0)
    print("#{} {}".format(test_case, num_max))