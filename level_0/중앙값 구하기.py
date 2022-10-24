# Title : 중앙값 구하기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120811

def solution(array):
    answer = 0
    array.sort()
    answer = array[len(array)//2]
    return answer