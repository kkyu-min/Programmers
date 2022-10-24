# Title : 각도기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120829

# 파이썬에서는 && 대신 and 사용

def solution(angle):
    answer = 0
    if angle>0 and angle<90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle>90 and angle<180:
        answer = 3
    else:
        answer = 4
    return answer