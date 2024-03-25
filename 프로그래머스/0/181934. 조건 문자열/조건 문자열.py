def solution(ineq, eq, n, m):
    if eq == "=":
        if n == m:
            return 1
    if ineq == "<":
        if n < m:
            return 1
        else:
            return 0
    else:
        if n > m:
            return 1
        else:
            return 0