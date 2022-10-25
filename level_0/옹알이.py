# Title : 옹알이
# Date : 2022/10/25
# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    answer = 0
    res_list = []
    for bab in babbling:
        if "aya" in bab :
            bab = bab.replace("aya",'1')
        if "ye" in bab:
            bab = bab.replace("ye","2")
        if "woo" in bab:
            bab = bab.replace("woo","3")
        if "ma" in bab:
            bab = bab.replace("ma","4")
        res_list.append(bab)
    for res in res_list:
        tmp = 1
        if res.isdigit():
            for i in range(len(res)-1):
                if res[i] != res[i+1]:
                    tmp += 1
        else:
             tmp = 0
        if tmp == len(res):
            answer += 1
    return answer