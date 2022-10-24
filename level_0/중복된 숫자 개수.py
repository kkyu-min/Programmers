# Title : 중복된 숫자 개수
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120583

# 파이썬 배열 함수
# len() -> 배열 길이 반환
# count(n) - > 배열 내 n의 개수 반환 

def solution(array, n):
    answer = 0
    for i in array:
        if i == n :
            answer += 1
    return answer