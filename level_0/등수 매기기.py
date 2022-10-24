# Title : 등수 매기기
# Date : 2022/10/24
# https://school.programmers.co.kr/learn/courses/30/lessons/120882

def solution(score):
    answer = []
    avg = []
    for x,y in score:
        avg.append((x+y)/2)
        answer.append(1)
    for i in range(len(avg)):
        rank = 0
        for j in range(len(avg)):
            if avg[j] > avg[i]:
                rank += 1
        answer[i] += rank
    return answer