import math

def solution(dots):
    answer = 0
    for i in range(1, len(dots)):
        dotli = dots[:]
        dy = dotli[0][1] - dotli[i][1]
        dx = dotli[0][0] - dotli[i][0]
        if dx == 0:
            angli1 = 90
        else:
            angle = int(math.atan(dy/dx) * (180/math.pi))
            if dx < 0:
                angle += 180
            elif dy < 0:
                angle += 360
            angli1 = angle % 180
        
        dotli.pop(i)
        dotli.pop(0)
        
        dy = dotli[0][1] - dotli[1][1]
        dx = dotli[0][0] - dotli[1][0]
        if dx == 0:
            angli2 = 90
        else:
            angle = int(math.atan(dy/dx) * (180/math.pi))
            if dx < 0:
                angle += 180
            elif dy < 0:
                angle += 360
            angli2 = angle % 180
        
        if angli1 == angli2:
            answer = 1
        
    return answer