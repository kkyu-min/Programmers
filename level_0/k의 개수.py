# Title : k의 개수
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120887

def solution(i, j, k):
    answer = 0
    nums = [str(x) for x in range(i,j+1)]
    for num in nums:
        if str(k) in num:
            answer += num.count(str(k))
    return answer