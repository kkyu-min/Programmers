# Title : 중복된 문자 제거
# Date : 2022/10/20
# https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    answer = []
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] not in answer:
            answer.append(my_string[i])
    answer = ''.join(answer)
    return answer