# Title : A로 B 만들기
# Date : 2022/10/20
# https://school.programmers.co.kr/learn/courses/30/lessons/120886

def solution(before, after):
    answer = 0
    if sorted(before) == sorted(after):
        answer = 1
    return answer