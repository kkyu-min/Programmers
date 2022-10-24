# Title : 유한소수 판별하기
# Date : 2022/10/23
# https://school.programmers.co.kr/learn/courses/30/lessons/120878

from fractions import Fraction
def solution(a, b):
    answer = 2
    frac = Fraction(a,b)
    num = frac.denominator
    if num == 1:
        return 1
    tmp = []
    d = 2 
    while d <= num:
        if num % d == 0:
            if d not in tmp:
                tmp.append(d)
            num = num // d
        else:
            d += 1
    if len(tmp) == 2:
        if tmp.count(2) + tmp.count(5) == 2:
            answer = 1
    elif len(tmp)==1:
        if tmp.count(2) + tmp.count(5) == 1:
            answer = 1
    return answer