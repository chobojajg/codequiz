def fibonacci(n):
    f = [0]*(n + 1)
    f[1] = 1
    if n >= 2:
        f[2] = 1
        for i in range(3, n+1):
            f[i] = f[i - 1] + f[i - 2]  # 코드2
    return f[n]


n = int(input())
print(fibonacci(n))