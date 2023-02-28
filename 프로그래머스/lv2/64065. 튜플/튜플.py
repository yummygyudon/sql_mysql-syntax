import re
def solution(s):
    rmCover = s[2:len(s)-2]
    # print(rmCover)
    elements = list(rmCover.split("},{"))
    elements = [list(s.split(",")) for s in elements]
    # print(elements)
    elements.sort(key = lambda x : len(x))
    # print(elements)
    
    answer = []
    for elem in elements :
        for e in elem :
            if e in answer :
                continue
            else :
                answer.append(e)
    # print(answer)
    return list(map(int,answer))