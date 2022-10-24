# Title : 외계행성의 나이
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120834

# 파이썬 함수 활용
# def solution(age):
#     return ''.join([chr(97+int(i)) for i in str(age)])

# 내 풀이
def solution(age):
    answer = ''
    for i in str(age):
        answer += chr(97+int(i))
    return answer