# Title : 모스부호(1)
# Date : 2022/10/21
# https://school.programmers.co.kr/learn/courses/30/lessons/120838

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    answer = ''
    list_letter = letter.split()
    for ltr in list_letter:
        answer += morse[ltr]
    return answer