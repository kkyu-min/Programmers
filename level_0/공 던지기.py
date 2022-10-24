# Title : 공 던지기
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    answer = 0
    index = 0
    for i in range(k-1):
        index += 2
        if index - len(numbers) == 0:
            index = 0
        elif index - len(numbers) == 1:
            index = 1
    answer = numbers[index]
    return answer