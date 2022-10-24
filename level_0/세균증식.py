# Title : 세균 증식
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120910

def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2
    return answer