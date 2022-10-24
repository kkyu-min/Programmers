# Title : 숨어있는 숫자의 덧셈(1)
# Date : 2022/10/19
#https://school.programmers.co.kr/learn/courses/30/lessons/120851

# 파이썬 함수 사용 isdigit()
# def solution(my_string):
#     answer = 0
#     for str in my_string:
#         if str.isdigit():
#             answer += int(str)
#     return answer

# 내 풀이
import re
def solution(my_string):
    answer = 0
    my_str = re.findall(r'\d', my_string)
    for str in my_str:
        answer += int(str)
    return answer