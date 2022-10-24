# Title : 옷가게 할인 받기
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120818

def solution(price):
    answer = 0
    if price >= 100000 and price < 300000:
        answer = price * 0.95
    elif price >= 300000 and price <500000:
        answer = price * 0.9
    elif price >= 500000:
        answer = price * 0.8
    else:
        answer = price
    return int(answer)