# Title : 배열의 평균값
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120817


# 파이썬 함수 사용하기
# def solution(numbers):
#   answer = sum(numbers) / len(numbers)
  
# 내 풀이
def solution(numbers):
    answer = 0
    for number in numbers:
        answer += number
    answer /= len(numbers)
    return answer