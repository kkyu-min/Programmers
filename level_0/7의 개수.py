# Title : 7의 개수
# Date :2022/10/20
# https://school.programmers.co.kr/learn/courses/30/lessons/120912

# 파이썬 함수 사용 하기!!
# def solution(array):
#   return ''.join(map(str,array)).count('7')

# 내 풀이
def solution(array):
    answer = 0
    for arr in array:
        for i in range(len(str(arr))):
            if str(arr)[i] == '7':
                answer += 1
    return answer
  