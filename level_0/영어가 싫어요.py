# Title : 영어가 싫어요
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    english = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    answer = ''
    tmp = 0
    for i in range(len(numbers)):
        if numbers[tmp:i+1] in english:
            answer += english[numbers[tmp:i+1]]
            tmp = i+1
    answer = int(answer)
    return answer