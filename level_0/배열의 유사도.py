# Title : 배열의 유사도
# Date : 2022/10/19
# 

# set 함수 활용
def solution(s1,s2):
  return len(set(s1)&set(s2))

# 내 풀이
def solution(s1, s2):
    answer = 0
    for str in s1:
        if str in s2:
            answer += 1
    return answer