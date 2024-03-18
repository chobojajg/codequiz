def solution(numer1, denom1, numer2, denom2):
    answer = []
    num = (denom1 * numer2) + (numer1 * denom2)
    den = denom1 * denom2
    
    minnum = min(num, den)
    maxnum = max(num, den)
    minarr = [1]
    maxarr = [1]    
    divarr = []
    divnum = 1
    
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
        
    answer.append(num // divnum)
    answer.append(den // divnum)
    
    return answer