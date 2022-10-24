# Title : 최빈값 구하기
# Date : 2022/10/23
# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    answer = 0
    numbers = set(array)
    cnt = 0
    for number in numbers:
        if array.count(number) > cnt:
            cnt = array.count(number)
            answer = number
        elif array.count(number) == cnt:
            answer = -1
    return answer