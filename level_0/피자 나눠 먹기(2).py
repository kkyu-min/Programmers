# Title : 피자 나눠 먹기(2)
# Date : 2022/10/20
# https://school.programmers.co.kr/learn/courses/30/lessons/120815

import math

def solution(n):
    answer = n * 6 // math.gcd(n,6) // 6
    return answer