# Title : 이진수 더하기
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120885

def solution(bin1, bin2):
    answer = ''
    tmp = int(bin1,2) + int(bin2,2)
    if tmp == 0:
        answer = '0'
    while tmp > 0:
        if tmp % 2 != 0:
            answer += '1'
            tmp = tmp // 2
        else:
            answer += '0'
            tmp = tmp // 2
    answer = answer[::-1]
    return answer