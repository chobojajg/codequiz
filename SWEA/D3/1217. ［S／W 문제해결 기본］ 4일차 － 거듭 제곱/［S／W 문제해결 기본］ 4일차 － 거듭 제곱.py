def my_power(num, cnt):
    result = num
    if cnt > 1:
        result = result * my_power(num, cnt - 1)
    return result

T = 10
for test_case in range(1, T + 1):
    case = int(input())
    num, cnt = map(int, input().split())
    result = my_power(num, cnt)
    print(f'#{case} {result}')
