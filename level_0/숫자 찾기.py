# Title : 숫자 찾기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    answer = -1
    tmp = len(str(num)) + 1
    while num > 0:
        tmp -= 1
        if num % 10 == k:
            answer = tmp
        num = num // 10
    return answer