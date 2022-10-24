# Title : 문자열 정렬하기(1)
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    answer = []
    for str in my_string:
        if str.isdigit():
            answer.append(int(str))
    answer.sort()
    return answer