import sys
n = int(sys.stdin.readline())
arr = []
cnt = 0
while True:
    d = int(sys.stdin.readline())
    if d == -1:
        if len(arr) == 0:
            print("empty")
        else:
            for i in arr:
                print(i, end=' ')
        break

    if d == 0:
        arr.pop(0)
        cnt -= 1
    else:
        if cnt < n:
            arr.append(d)
            cnt += 1