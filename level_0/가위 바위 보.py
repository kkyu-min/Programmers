# Title : 가위 바위 보
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    answer = ''
    for str in rsp:
        if str == "2":
            answer += "0"
        elif str == "0":
            answer += "5"
        else:
            answer += "2"
    return answer