"""
* 한 음악을 반복해서 재생할 때도 있어 -> 기억하고 있는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다

* 음 : C, C#, D, D#, E, F, F#, G, G#, A, A#, B (12개)
* [제목, 시작 시각, 종료 시간, 악보]
* 1분에 음 1개
    - 음악은 반드시 처음부터 재생
    - 음악 길이보다 재생 시간이 길 경우 : 처음부터 반복 재생(끊김 X)
    - 음악 길이보다    "     짧은 경우 : 처음부터 재생시간만큼
    
* 조건 일치 음악이 여러 개일 때 : 재생된 시간이 제일 긴 음악 제목 반환
    - 재생 시간까지 같을 떼 : 먼저 입력된 음악 제목
* 조건 일치 음악이 아예 없을 떄 : (None)
"""
# 기억하는 음, [시작 시각, 끝 시각, 제목, 악보]
def solution(m, musicinfos):
    remMelody = makeLyric(m)
    print("기억하는 음 : ",remMelody)
    # print(getPlayTime("22:50", "23:10"))
    # candidate = []
    BEST = None
    # print(["A","B","C","D"] in ["G","K","S","A","B","C","D","F","J",'G'])
    for info in musicinfos :
        info = list(info.split(','))
        start = list(map(int,info[0].split(":")))
        end = list(map(int,info[1].split(":")))
        start = start[0]*60 + start[1]
        end = end[0]*60 + end[1]
        playTime = end-start
        
        lyric = makeLyric(info[3])
        print("lyric : ", lyric)
        lyric = fitting(playTime, lyric)
        print(lyric)
        if not matching(remMelody, lyric) :
            continue
        if BEST == None or (BEST[0] < playTime) or (BEST[0] == playTime and BEST[2] > start)  :
            BEST = [playTime, info[2], start]

    if BEST :
        return BEST[1]
    return "(None)"

MAPPING = [["C#","c"],["D#","d"],["F#","f"],["G#","g"],["A#","a"]]
def makeLyric(melody : str) :
    for i in range(5) :
        melody = melody.replace(MAPPING[i][0], MAPPING[i][1])
    return melody
        
    
def matching(remMelody : str, musicMelody : str) :
    return remMelody in musicMelody

import math
def fitting(playTime, matchMelody) :
    
    # matchMelody =  matchMelody * (1439//len(matchMelody))
    matchMelody *= math.ceil(playTime/len(matchMelody))
    # print(matchMelody)
    return matchMelody[:playTime]
    
def getPlayTime(startTime, endTime) :
    start = list(map(int,startTime.split(":")))
    end = list(map(int,endTime.split(":")))
    start = start[0]*60 + start[1]
    end = end[0]*60 + end[1]
    return end-start
    
    