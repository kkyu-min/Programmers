# Title : 제곱수 판별하기
# Datee : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120909

def solution(n):
    answer = 2
    num = 1
    while num ** 2<=n:
        if num ** 2 == n:
            answer = 1
        num += 1
    return answer