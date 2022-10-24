# Title : 로그인 성공?
# Date : 2022/10/24
# https://school.programmers.co.kr/learn/courses/30/lessons/120883

def solution(id_pw, db):
    answer = ''
    for x,y in db:
        if x == id_pw[0]:
            if y == id_pw[1]:
                answer = "login"
                return answer
            else:
                answer = "wrong pw"
                return answer
        else:
            answer = "fail"
    return answer