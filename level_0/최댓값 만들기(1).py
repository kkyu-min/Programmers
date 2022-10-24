# Title : 최댓값 만들기(1)
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120847

def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer