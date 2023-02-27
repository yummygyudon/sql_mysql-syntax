def findParent(elem) :
    # if PARENT[elem] != elem :
    #     PARENT[elem] =  findParent(elem)
    # return PARENT[elem]
    if PARENT[elem] == elem :
        return elem
    PARENT[elem] = findParent( PARENT[elem] )
    return PARENT[elem]

def unionParent(elemA, elemB) :
    elemA = findParent(elemA)
    elemB = findParent(elemB)
    if elemA == elemB :
        return
    if elemA < elemB :
        PARENT[elemB] = elemA
    else :
        PARENT[elemA] = elemB
        
V, E = map(int,input().split())
PARENT = [0] * (V+1)

EDGES =[]
RESULT = 0

for i in range(1, V+1) :
	PARENT[i] = i

for _ in range(E) :
	a, b, cost = map(int, input().split())
	EDGES.append([cost, a, b])
    
EDGES.sort()
last = 0
    
for edge in EDGES :
    cost, a, b = edge
    if findParent(a) != findParent(b) :
        unionParent(a,b)
        RESULT += cost
        last = cost

print(RESULT - last)