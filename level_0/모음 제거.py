# Title : 모음 제거
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    answer = ''
    vowel = {'a','e','i','o','u'}
    for str in my_string:
        if str not in vowel:
            answer += str
    return answer