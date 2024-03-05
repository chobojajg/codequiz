a = int(input())
check = 0
while True:
    bun = check + sum(int(i) for i in str(check))
    if bun == a:
        break
    if check > a:
        check = 0
        break
    check = check + 1
print(check)