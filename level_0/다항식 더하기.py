# Title : 다항식 더하기
# Date : 2022/10/24
# https://school.programmers.co.kr/learn/courses/30/lessons/120863

def solution(polynomial):
    answer = ''
    poly = polynomial.split(' ')
    const = 0
    var = 0
    for i in range(0,len(poly),2):
        if 'x' not in str(poly[i]):
            const += int(poly[i])
        else:
            if len(poly[i]) == 1:
                var += 1
            else:
                tmp = poly[i].replace('x','')
                var += int(tmp)
    if const == 0:
        if var == 1:
            answer = 'x'
        elif var == 0:
            answer = ''
        else:
            answer = str(var) + "x"
    else:
        if var == 0:
            answer = str(const)
        elif var == 1:
            answer = 'x + ' + str(const)
        else:
            answer = str(var) + 'x + ' + str(const)
    return answer
