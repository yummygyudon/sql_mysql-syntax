def solution(triangle):
    for i in range(1, len(triangle)):
        for k in range(len(triangle[i])) :
            if k == 0 : # 왼쪽 끝 값일 때
                triangle[i][k] += triangle[i-1][k]
            elif k == len(triangle[i])-1 :
                triangle[i][k] += triangle[i-1][k-1]
            else :
                triangle[i][k] += max(triangle[i-1][k], triangle[i-1][k-1])
    return max(triangle[-1])