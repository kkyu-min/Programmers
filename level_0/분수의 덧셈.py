# Title : 분수의 덧셈
# Date : 2022/10/19
# https://school.programmers.co.kr/learn/courses/30/lessons/120808

# 더 나은 풀이
# 유리수 계산 시 분수로 표현
# from fractions import Fraction

# from fractions import Fraction

# def solution(denum1, num1, denum2, num2):
#   answer = Fraction(denum1,num1) + Fraction(denum2, num2)
#   return [answer.numerator, answer.denominator]



# 내 풀이
def gcd(x,y):
    if x > y:
        while x % y != 0:
            mod = x % y
            x = y
            y = mod
        return y
    else:
        while y % x != 0:
            mod = y % x
            y = x
            x = mod
        return x
def solution(denum1, num1, denum2, num2):
    answer = []
    # 분모의 최소 공배수 구하기
    g1 = gcd(num1,num2)
    num = (num1 * num2) // g1
    denum = denum1*(num2//g1) + denum2*(num1//g1)
    g2 = gcd(denum, num)
    
    answer.append(denum//g2)
    answer.append(num//g2)
    return answer