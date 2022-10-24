# Title : 인덱스 바꾸기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120895

# 파이썬 함수 활용
# def solution(my_string, num1, num2):
#   s = list(my_string)
#   s[num1],s[num2] = s[num2],s[num1]
#   answer = ''.join(s)
#   return answer

def solution(my_string, num1, num2):
    my_list = list(my_string)
    tmp1 = my_list[num1]
    tmp2 = my_list[num2]
    my_list[num1] = tmp2
    my_list[num2] = tmp1
    answer = "".join(my_list)
    return answer