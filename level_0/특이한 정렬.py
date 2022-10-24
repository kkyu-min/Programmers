# Title : 특이한 정렬
# Date : 2022/10/23
# https://school.programmers.co.kr/learn/courses/30/lessons/120880

def solution(numlist, n):
    answer = [i-n for i in numlist]
    answer = sorted(answer,key=abs)
    for i in range(1,len(answer)):
        if abs(answer[i-1]) == abs(answer[i]):
            if answer[i-1] < answer[i]:
                answer[i-1],answer[i] = answer[i],answer[i-1]
    for i in range(len(answer)):
        answer[i] += n
    return answer