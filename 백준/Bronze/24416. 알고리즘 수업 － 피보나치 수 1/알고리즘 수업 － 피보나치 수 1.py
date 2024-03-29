num = int(input())
cnt1 = 0
cnt2 = 0


def fib(n):
    global cnt1
    if n == 1 or n == 2:
        return 1 # 코드1
    else:
        cnt1 += 1
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global cnt2
    f = [0]*(n+1)
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        f[i] = f[i - 1] + f[i - 2] # 코드2
        cnt2 += 1
    return f[n]


fib(num)
fibonacci(num)
print(f'{cnt1 + 1} {cnt2}')