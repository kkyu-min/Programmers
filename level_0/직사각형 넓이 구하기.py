# Title : 직사각형 넓이 구하기
# Date : 2022/10/24
# https://school.programmers.co.kr/learn/courses/30/lessons/120860

def solution(dots):
    answer = 0
    dots.sort(key=lambda x:x[0])
    answer = abs(dots[0][1] - dots[1][1]) * abs(dots[0][0] - dots[2][0])
    return answer