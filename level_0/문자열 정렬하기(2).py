# Title : 문자열 정렬하기(2)
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120911

# 파이썬 함수 사용 .join()
# "구분자".join(리스트) -> 리스트를 문자열로 만들어줌
# def solution(my_string):
#     answer = ''.join(sorted(my_string.lower()))
                   
# 내 풀이
def solution(my_string):
    answer = ''
    my_string = sorted(my_string.lower())
    for str in my_string:
        answer += str
    return answer