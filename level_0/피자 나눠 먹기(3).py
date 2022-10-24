# Title : 피자 나눠 먹기(3)
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(slice, n):
    answer = 0
    if n % slice == 0:
        answer = n // slice
    else:
        answer = n // slice + 1
    return answer