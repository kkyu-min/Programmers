# Title : 잘라서 배열로 저장하기
# Date : 2022/10/20
# https://school.programmers.co.kr/learn/courses/30/lessons/120913

import math
def solution(my_str, n):
    answer = []
    for i in range(math.ceil(len(my_str)/n)):
        answer.append(my_str[i*n:i*n+n:])
    return answer