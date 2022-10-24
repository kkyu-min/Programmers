# Title : 소인수분해
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120852

def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            if d not in answer:
                answer.append(d)
            n = n // d
        else:
            d += 1
    return answer