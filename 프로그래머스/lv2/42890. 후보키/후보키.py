"""
"유일성" 검사 테스트 : 식별 가능 -> set로 
"최소성" 검사 테스트 : 식별하는데 꼭 필요한 속성들로만 구성되어어야 함. -> 모든 속성 경우의 수
"""

def solution(relation):
    attributeCnt = len(relation[0])
    tupleCnt = len(relation)
    
    uniqueCase = []
    
    case = 1
    while case < (1 << attributeCnt) :
        # print("case : ",case," == 현재에 해당하는 Binary : ", bin(case))
        checkSet = set()
        # 이번 1이 켜져있는 위치의 컬럼을 사용하는 경우의 수
        # 모든 행에 대해 해당 경우의 수를 확인해봐야함
        for row in range(tupleCnt) :
            caseValueOfEachTuple = ''
            # 각 행의 각 컬럼 확인
            for colNum in range(attributeCnt) :
                # 해당 while에서 돌며 확인하는 case와 일치하는 위치의 컬럼값 +=
                if case & (1 << colNum) :
                    caseValueOfEachTuple += relation[row][colNum]
            checkSet.add(caseValueOfEachTuple)
        # print(checkSet)
        
        """
        만약 각 case에 대하여 각 행에서 해당 컬럼값들을 조합한 값들이 서로 독립적이면
        len(checkSet)과 행 수가 같아야함.
        """
        # 유일성
        if len(checkSet) == tupleCnt :
            isUnique = True
            for existCase in uniqueCase :
                # 최소성 
                """
                이미 이번 조합에서 포함된 컬럼들로
                이전에 최소한의 컬럼조합으로 유일성을 보장한 적이 있음
                
                순회하기 때문에 existCase가 "case보다 작을 수밖에 없음"
                """
                if (existCase & case) == existCase :
                    # print("existCase : ",existCase," | case : ",case)
                    isUnique = False
                    break
            if isUnique :
                uniqueCase.append(case)
            # uniqueCase.append(case)
        # print(uniqueCase)
        case += 1
        
        # print()
    answer = 0
    return len(uniqueCase)

# def solution(relation):
#     answer_list = list()
#     attributeCnt = len(relation[0])
#     tupleCnt = len(relation)
#     for i in range(1, 1 << len(relation[0])):
#         print("case : ",i," == 현재에 해당하는 Binary : ", bin(i))
#         tmp_set = set()
#         for j in range(tupleCnt):
#             tmp = ''
#             for k in range(attributeCnt):
#                 if i & (1 << k):
#                     tmp += str(relation[j][k])
#             tmp_set.add(tmp)
#         print(tmp_set)
#         if len(tmp_set) == len(relation):
#             not_duplicate = True
#             for num in answer_list:
                
#                 if (num & i) == num:
#                     not_duplicate = False
#                     break
#             if not_duplicate:
#                 answer_list.append(i)
#         print(answer_list)
#         print()
#     return len(answer_list)

# def getNumOfCase(elemCnt) :
#     if elemCnt == 1 :
#         return 1
#     return elemCnt * getNumOfCase(elemCnt-1)