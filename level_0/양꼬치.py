# Title : 양꼬치
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    answer = n * 12000 + k * 2000 - n // 10 * 2000
    return answer