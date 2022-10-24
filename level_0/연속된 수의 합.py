# Title : 연속된 수의 합
# Date : 2022/10/24
# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    answer = []
    tmp = 0
    for i in range(num):
        tmp += i
    x = (total - tmp) // num
    for i in range(num):
        answer.append(x+i)
    return answer