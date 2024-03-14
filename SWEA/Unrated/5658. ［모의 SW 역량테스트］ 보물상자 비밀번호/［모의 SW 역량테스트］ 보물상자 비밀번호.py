T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    num_list = list(input())
    all_list = []
    rot = n // 4
    for _ in range(rot):
        temp = []
        for i in range(n):
            temp.append(num_list[i])
            if len(temp) == rot:
                all_list.append(''.join(temp))
                temp = []
        num_list.append(num_list.pop(0))
    all_list = list(set(all_list))
    for i in range(len(all_list)):
        all_list[i] = int(all_list[i], 16)
    all_list.sort(reverse=True)
    result = all_list[k-1]
    print(f'#{test_case} {result}')