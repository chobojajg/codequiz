from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 0
    break_check = 0
    for i in range(1, n + 1):
        check_over_num = 0
        all_list = list(combinations(lst, i))
        for i in range(len(all_list)):
            e_sum = sum(all_list[i])
            if e_sum > k:
                check_over_num += 1
            if e_sum == k:
                result += 1
            if check_over_num == len(all_list):
                break_check = 1
                break
        if break_check == 1:
            break
    print(f'#{test_case} {result}')