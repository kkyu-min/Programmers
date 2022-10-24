# Title : 외계어 사전
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    answer = 0
    for str in dic:
        tmp = 0
        for i in range(len(spell)):
            if spell[i] in str:
                tmp += 1
        if tmp == len(spell):
            answer = 1
            break
        else:
            answer = 2
    return answer