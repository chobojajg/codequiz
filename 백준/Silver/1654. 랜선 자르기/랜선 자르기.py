k, n = map(int, input().split())
lis = []
for _ in range(k):
    lis.append(int(input()))


def cut_line(arr, key):
    result = 0
    for i in arr:
        result += i // key
    return result


def binary_search(arr, low, high, line_need):
    if low > high:
        return high

    line_len = (high + low) // 2
    make = cut_line(arr, line_len)

    if make >= line_need:
        return binary_search(arr, line_len + 1, high, line_need)
    else:
        return binary_search(arr, low, line_len - 1, line_need)


print(binary_search(lis, 1, max(lis), n))