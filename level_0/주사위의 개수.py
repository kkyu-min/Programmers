# Title : 주사위의 개수
# Date : 2022/10/20
# https://school.programmers.co.kr/learn/courses/30/lessons/120845

def solution(box, n):
    answer = (box[0] // n ) * (box[1] // n ) * (box[2] // n )
    return answer