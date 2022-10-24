# Title : 배열 회전시키기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120844

# 파이썬 함수 활용
# 배열 슬라이싱 해서 사용
def solution(numbers, direction):
  return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]

# 내 풀이
def solution(numbers, direction):
    if direction == "left":
        tmp = numbers[0]
        for i in range(1,len(numbers)):
            numbers[i-1] = numbers[i]
        numbers[-1] = tmp
    else:
        tmp = numbers[-1]
        numbers.pop(-1)
        numbers.insert(0,tmp)
    return numbers