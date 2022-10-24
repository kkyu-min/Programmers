# Title : 최댓값 만들기
# Date : 2022/10/20
# https://school.programmers.co.kr/learn/courses/30/lessons/120862

# 파이썬 함수 활용
# max()
# def solution(numbers):
#   numbers.sort()
#   return max(numbers[0] * numbers[1], numbers[-2] * numbers[-1])

# 내 풀이
def solution(numbers):
    answer = 0
    numbers.sort()
    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
        answer = numbers[0] * numbers[1]
    else:
        answer = numbers[-1] * numbers[-2]
    return answer