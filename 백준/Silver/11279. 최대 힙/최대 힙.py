import sys
import heapq
n = int(input())
arr = []
for _ in range(n):
    s = int(sys.stdin.readline())
    if s == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -s)