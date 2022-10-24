# Title : 자릿수 더하기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120906

# 파이썬 함수 사용
def solution(n):
  answer = sum(list(map(int,str(n))))

# 내 풀이
def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n = n //10 
    return answer