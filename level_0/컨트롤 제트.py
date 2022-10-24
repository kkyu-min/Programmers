# Title : 컨트롤 제트
# Date : 2022/10/23
# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    answer = 0
    cal = s.split(' ')
    tmp = []
    for i in range(len(cal)):
        if cal[i] == 'Z':
            if len(tmp) == 0:
                continue
            else:
                answer -= tmp.pop()
        else:
            tmp.append(int(cal[i]))
            answer += int(cal[i])
    return answer