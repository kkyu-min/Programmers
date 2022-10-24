# Title : 한 번만 등장한 문자
# Date : 2022/10/20
# https://school.programmers.co.kr/learn/courses/30/lessons/120896

def solution(s):
    answer = ''
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            answer += s[i]
    answer = ''.join(sorted(answer))
    return answer