from collections import deque
DEPTH = 0
TARGET = 0
NUMBERS = []
MIN = 1e9
COUNT = 0
def solution(numbers, target):
    global DEPTH, TARGET, NUMBERS
    DEPTH = len(numbers)
    TARGET = target
    NUMBERS = numbers
    # answer = 0
    # q = deque()
    # q.append()
    dfs(0,0)
    print(COUNT)
    return COUNT

def dfs(depth, num) :
    global MIN, COUNT
    # if num == TARGET :
    #     MIN = min(depth, MIN)
    #     return
    if depth == DEPTH :
        if num == TARGET :
            COUNT += 1
        return
    dfs(depth+1, num+NUMBERS[depth])
    dfs(depth+1, num-NUMBERS[depth])