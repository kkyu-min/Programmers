# Title : 안전지대
# Date : 2022/10/25
# https://school.programmers.co.kr/learn/courses/30/lessons/120866

def solution(board):
    answer = 0
    vir = [[0 for j in range(len(board)+2)] for i in range(len(board)+2)]
    for i in range(1,len(board)+1):
        for j in range(1,len(board)+1):
            if board[i-1][j-1] == 1:
                vir[i-1][j-1] = 1
                vir[i-1][j] = 1
                vir[i-1][j+1] = 1
                vir[i][j-1] = 1
                vir[i][j] = 1
                vir[i][j+1] = 1
                vir[i+1][j-1] = 1
                vir[i+1][j] = 1
                vir[i+1][j+1] = 1
    for i in range(len(board)):
        for j in range(len(board)):
            if vir[i+1][j+1] == 0:
                answer += 1
    return answer