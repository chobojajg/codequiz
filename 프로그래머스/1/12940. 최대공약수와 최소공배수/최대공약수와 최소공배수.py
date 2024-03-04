def solution(n, m):
    answer = []
    minnum = min(n, m)
    maxnum = max(n, m)
    minarr = [1]
    maxarr = [1]
    divarr = []
    divnum = 1
    subarr = []
    subnum = 1
    
    #minarr 구하기
    a = minnum
    for i in range(2, minnum + 1):
        while(a % i == 0):
            minarr.append(i)
            a = a / i
    
    #maxarr 구하기
    b = maxnum
    for i in range(2, maxnum + 1):
        while(b % i == 0):
            maxarr.append(i)
            b = b / i
    
    #최대공약수 divnum
    dmin = minarr[:]
    dmin.sort(reverse = True)
    dmax = maxarr[:]
    dmax.sort(reverse = True)
    for i in range(len(dmin)):
        for j in range(len(dmax)):
            if dmin[i] == 1:
                break;
            if dmin[i] == dmax[j]:
                divnum = divnum * dmin[i]
                dmin[i] = 1
                dmax[j] = 1
                break
    
    #최소공배수 subnum
    smin = minarr[:]
    smax = maxarr[:]
    for i in range(len(smin)):
        for j in range(len(smax)):
            if smin[i] == smax[j]:
                subnum = subnum * smin[i]
                smin[i] = 1
                smax[j] = 1
    subarr = smin + smax
    for i in subarr:
        subnum = subnum * i
    
    answer.append(divnum)
    answer.append(subnum)
    
    return answer