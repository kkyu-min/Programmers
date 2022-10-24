# Title : 가장 큰 수 찾기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120899

def solution(array):
    answer = [max(array), array.index(max(array))]
    return answer