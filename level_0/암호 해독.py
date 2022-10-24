# Title : 암호 해독
# Date : 2022/10/20
# https://school.programmers.co.kr/learn/courses/30/lessons/120892

# 파이썬 함수
# 인덱스 슬라이싱
# def solution(cipher, code):
#   answer =''
#   for i in range(code-1,len(cipher),code):
#     answer += cipher[i]
#   return answer

# 내 풀이
def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)):
        if i % code == code - 1:
            answer += cipher[i]
    return answer