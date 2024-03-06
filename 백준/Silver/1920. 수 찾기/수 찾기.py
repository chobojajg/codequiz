def binarySearch(arr, low, high, key):
    if low > high:
        return print(0)
    mid = int(low + (high - low) / 2)

    if arr[mid] == key:
        return print(1)
    elif arr[mid] > key:
        return binarySearch(arr, low, mid - 1, key)
    else:
        return binarySearch(arr, mid + 1, high, key)


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
max_a = max(a)
min_a = min(a)
a.sort()

for i in b:
    if i > max_a or i < min_a:
        print(0)
        continue
    binarySearch(a, 0, len(a), i)