# Title : 문자 반복 출력하기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    answer = ''
    for str in my_string:
        for i in range(n):
            answer += str
    return answer