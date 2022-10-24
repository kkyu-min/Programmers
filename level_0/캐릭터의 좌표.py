# Title : 캐릭터의 좌표
# Date : 2022/10/24"
# https://school.programmers.co.kr/learn/courses/30/lessons/120861

def solution(keyinput, board):
    answer = [0,0]
    for i in range(len(keyinput)):
        if keyinput[i] == "left":
            if answer[0] <= board[0]//2 *(-1):
                continue
            else:
                answer[0] -= 1
        elif keyinput[i] == "right":
            if answer[0] >= board[0]//2:
                continue
            else:
                answer[0] += 1
        elif keyinput[i] == "up":
            if answer[1] >= board[1]//2:
                continue
            else:
                answer[1] += 1
        elif keyinput[i] == "down":
            if answer[1] <= board[1]//2 * (-1):
                continue
            else:
                answer[1] -= 1
    return answer