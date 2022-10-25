# Title : 겹치는 선분의 길이
# Date : 2022/10/25
# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    answer = 0
    line = []
    for x,y in lines:
        for i in range(x,y):
            line.append(i+0.5)
    for x in set(line):
        if line.count(x) >=2:
            answer += 1
    return answer