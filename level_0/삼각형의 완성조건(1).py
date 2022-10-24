# Title : 삼각형의 완성조건(1)
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120889

def solution(sides):
    answer = 2
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        answer =1
    return answer