# Title : 평행
# Date : 2022/10/25
# https://school.programmers.co.kr/learn/courses/30/lessons/120875

def solution(dots):
    answer = 0
    if dots[1][0] == dots[0][0] and dots[2][0] == dots[3][0]:
        answer += 1
    elif dots[1][0] == dots[0][0] or dots[2][0] == dots[3][0]:
        answer += 0
    else:
        if (dots[1][1]-dots[0][1]) / (dots[1][0] - dots[0][0]) == (dots[3][1]-dots[2][1]) / (dots[3][0] - dots[2][0]):
            answer += 1
    
    if dots[2][0] == dots[0][0] and dots[3][0] == dots[1][0]:
        answer += 1
    elif dots[2][0] == dots[0][0] or dots[3][0] == dots[1][0]:
        answer += 0
    else:
        if (dots[2][1]-dots[0][1]) / (dots[2][0] - dots[0][0]) == (dots[3][1]-dots[1][1]) / (dots[3][0] - dots[1][0]):
            answer += 1
    
    if dots[3][0] == dots[0][0] and dots[2][0] == dots[1][0]:
        answer += 1
    elif dots[3][0] == dots[0][0] or dots[2][0] == dots[1][0]:
        answer += 0
    else:
        if (dots[3][1]-dots[0][1]) / (dots[3][0] - dots[0][0]) == (dots[2][1]-dots[1][1]) / (dots[2][0] - dots[1][0]):
            answer += 1
    if answer >= 1:
        answer = 1
    else:
        answer = 0
    return answer