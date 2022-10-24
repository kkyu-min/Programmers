# Title : 문자열안에 문자열
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120908

# 파이썬 함수 사용
# def solution(str1,str2):
#   if str2 in str1:
#     return 1
#   else:
#     return 2
  
# def solution(str1, str2):
#   if str1.count(str2):
#     return 1
#   else:
#     return 2
  
# 내 풀이
def solution(str1, str2):
    answer = 2
    for i in range(len(str1)):
        if str1[i] == str2[0]:
            if str2 == str1[i:i+len(str2)]:
                answer = 1
    return answer