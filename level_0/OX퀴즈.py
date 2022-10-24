# Title : OX퀴즈
# Date : 2022/10/24
# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    answer = []
    for q in quiz:
        tmp = q.split(' ')
        oper = tmp[0:-2]
        res = tmp[-1]
        oper = ''.join(oper)
        if eval(oper) == int(res):
            answer.append("O")
        else:
            answer.append("X")
    return answer
  
def solution(quiz):
    answer = []
    for q in quiz:
        oper, res = q.split('=')
        if eval(oper) == int(res):
            answer.append("O")
        else:
            answer.append("X")
    return answer