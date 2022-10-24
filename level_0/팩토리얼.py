# Title : 팩토리얼
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    answer = 0
    fac = 1
    for i in range(1,n+1):
        fac *= i
        if fac > n :
            answer = i - 1
            break
        elif fac == n :
            answer = i
            break
    return answer