# Title : 짝수 홀수 개수
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    answer = []
    tmp = 0
    for num in num_list:
        if num % 2 == 0:
            tmp += 1
    answer = [tmp, len(num_list)-tmp]
    return answer