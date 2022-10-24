# Title : 369게임
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120891

def solution(order):
    answer = 0
    for i in str(order):
        if i in {'3','6','9'}:
            answer += 1
    return answer