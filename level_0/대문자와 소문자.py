# Title : 대문자와 소문자
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    answer = ''
    for str in my_string:
        if str.isupper():
            answer += str.lower()
        else:
            answer += str.upper()
    return answer