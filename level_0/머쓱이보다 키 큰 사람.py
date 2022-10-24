# Title : 머쓱이보다 키 큰 사람
# Date : 2022/10/10
# https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    answer = 0
    for i in array:
        if height < i:
            answer += 1
    return answer