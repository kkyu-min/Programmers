# Title : 구슬을 나누는 경우의 수
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120840

def solution(balls, share):
    answer = 1
    for i in range(share):
        answer *= (balls - i)
        answer //= (i+1)
    return answer