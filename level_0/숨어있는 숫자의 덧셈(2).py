# Title : 숨어있는 숫자의 덧셈(2)
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120864

import re
def solution(my_string):
    answer = sum(map(int, re.findall(r'\d+',my_string)))
    return answer  