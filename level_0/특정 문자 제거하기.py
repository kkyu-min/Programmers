# Title : 특정 문자 제거하기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120826

# 파이썬 함수 사용 
# replace(a,b) -> a를 b로 변경
def solution(my_string, letter):
  return my_string.replace(letter, '')

# 내 풀이
def solution(my_string, letter):
    answer = ''
    for str in my_string:
        if letter != str:
            answer += str
    return answer