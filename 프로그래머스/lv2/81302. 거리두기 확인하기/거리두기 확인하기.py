"""
P = 사람
O = 빈 테이블
X = 파티션
"""
ROOM = []
ROOM_SIZE, ROOM_QUANT = 5,5
CHECK = [[False] * 5 for _ in range(5)]
# 위아래, 양옆, 대각선
TD_ONE = [[-1,0], [1,0], [0,-1], [0,1]]
TD_TWO = [[-2,0], [2,0], [0,-2], [0,2]]
C = [[-1,-1],[-1,1], [1,-1],[1,1]]

"""
왼쪽 위
오른쪽 위
왼쪽 아래
오른쪽 아래
"""
CHECK_C =[ [[-1,0],[0,-1]], 
           [[-1,0],[0,1]], 
           [[1,0],[0,-1]], 
           [[1,0],[0,1]] ]
from collections import deque
def solution(places):
    global ROOM
    for room in places :
        dispos = []
        for line in room :
            dispos.append(list(line))
        ROOM.append(dispos)
#    print(ROOM)
            
    answer = []
    for i in range(ROOM_QUANT):
#        print("----------")
 #       print("|| ROOM %d ||"%i)
        answer.append(checkRoom(ROOM[i]))
   # print(answer)
    return answer



def checkRoom(room) :
    isPossible = 1
    for i in range(ROOM_SIZE) :
        for k in range(ROOM_SIZE) :
            if room[i][k] == 'P' :
#                print("[확인위치] : (%d,%d)"%(i,k))
                if not isKeepWell(i,k,room) :
                    return 0
    return isPossible
    
def isKeepWell(y,x, room) :
    # isWell = True
    # check = CHECK
    # q = deque()
    # q.append([y,x])
    # check[y][x] = True
    # while q :
    #     y, x = q.popleft()
#    print("< 바로 위아래 방향 검사 >")
    for i in range(4) :
        ny = y+TD_ONE[i][0]
        nx = x+TD_ONE[i][1]
        if 0 <= ny < 5 and 0 <= nx < 5 :
            """
            붙어있으면 더 볼 것 없이 불가능
            """
            if room[ny][nx] == 'P':
                return False
#    print("통과!")
#    print("< 대각성 방향 검사 >")
    for i in range(4):
        ny = y+C[i][0]
        nx = x+C[i][1]
        if 0 <= ny < 5 and 0 <= nx < 5 :
            """
            만약 대각선에 사람이 있으면 -> 체크 한번 더
            """
            if room[ny][nx] == 'P':
                # for k in range(4) :
                    for j in range(2) :
                        c = CHECK_C[i][j]
                        # print(c)
                        """
                        대각선이 P 인데 X가 안쳐져 있으면 불가능
                        """
                        if room[y+c[0]][x+c[1]] != 'X' :
 #                           print(c)
                            return False
   # print("통과!")
   # print("< 위아래 두 칸 방향 검사 >")
    for i in range(4) :
        ny = y+TD_TWO[i][0]
        nx = x+TD_TWO[i][1]
        if 0 <= ny < 5 and 0 <= nx < 5 :
    #        print(" 현재위치 : (%d,%d)"%(ny,nx))
            if room[ny][nx] == 'P' :
                # for k in range(4) :
   #             print(" 검사위치 : (%d,%d)"%(y+TD_ONE[i][0],x+TD_ONE[i][1]))
                if room[y+TD_ONE[i][0]][x+TD_ONE[i][1]] != 'X' :
                    return False  
    # print("통과!")
    # print()
    return True
    
def distanceOf(pos1, pos2) :
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])