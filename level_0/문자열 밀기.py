# Title : 문자열 밀기
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    answer = -1
    for i in range(len(A)):
        A = A[-1] + A[0:len(A)-1]
        if B == A:
            answer = i+1
            if answer == len(A):
                answer = 0
            break
    return answer