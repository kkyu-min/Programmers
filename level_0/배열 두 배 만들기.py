# Title : 배열 두 배 만들기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120809

# lambda함수
# def solution(numbers):
#   answer = list(map(lambda x: x*2, numbers))
#   return answer

# lambda 매개변수 : 표현식 
# list(map(함수, 리스트))
# -> 리스트로부터 원소를 하나씩 꺼내 함수에 대입한 후 새로운 리스트에 담아줌

# 내 풀이
def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(number*2)
    return answer