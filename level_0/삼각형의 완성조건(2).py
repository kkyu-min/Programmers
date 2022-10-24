# Title : 삼각형의 완성조건(2)
# Date : 2022/10/24
# https://school.programmers.co.kr/learn/courses/30/lessons/120868

def solution(sides):
    answer = 0
    sides.sort()
    tmp1 = sides[1]
    while tmp1 <= sides[1] and (tmp1 + sides[0]) > sides[1]:
        answer += 1
        tmp1 -= 1
    tmp2 = sides[1] + 1
    while tmp2 < sides[0] + sides[1]:
        answer += 1
        tmp2 += 1
    return answer