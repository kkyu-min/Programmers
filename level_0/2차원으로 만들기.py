# Title : 2차원으로 만들기
# Date : 2022/10/20
# https://school.programmers.co.kr/learn/courses/30/lessons/120842

def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        answer.append(num_list[i*n:i*n+n:])
    return answer