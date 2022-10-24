# Title : 다음에 올 숫자
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120924

arr = [1,2,3,4]
print(arr.pop())

def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1] + (common[1] - common[0])
    else:
        answer = common[-1] * (common[1] // common[0])
    return answer
        