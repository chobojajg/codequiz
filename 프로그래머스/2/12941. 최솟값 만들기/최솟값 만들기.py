def solution(A,B):
    answer = 0
    
    A.sort(reverse = True)
    B.sort()
    
    for i in range(len(A)):
        answer = answer + (A[i] * B[i])

    return answer