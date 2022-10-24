# Title : 진료순서 정하기
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    answer = [0 for i in range(len(emergency))]
    for i in range(len(emergency)):
        tmp = max(emergency)
        index = emergency.index(tmp)
        answer[index] = i+1
        emergency[index] = 0
    return answer