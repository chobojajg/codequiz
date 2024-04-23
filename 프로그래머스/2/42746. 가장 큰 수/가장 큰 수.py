def solution(numbers):
    answer = ''
    lis = list(map(str, numbers))
    lis.sort(key=lambda x:x*4, reverse=True)
    answer = str(int(''.join(lis)))
    return answer