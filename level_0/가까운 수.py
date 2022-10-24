# Title : 가까운 수
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    answer = array[0]
    for i in range(len(array)):
        if abs(answer - n) > abs(array[i] - n):
            answer = array[i]
        elif abs(answer - n) == abs(array[i] - n):
            answer = min(answer,array[i])
    return answer