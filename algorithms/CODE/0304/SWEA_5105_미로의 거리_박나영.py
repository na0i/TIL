import sys
sys.stdin = open('miro.txt', 'r')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    Q = [(r, c)]
    dist[r][c] = 0

    while Q:
        # 현재 위치
        curr_r, curr_c = Q.pop(0)
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if miro[nr][nc] == 1 or dist[nr][nc] != 0:
                continue
            # 3일때 갔던 거리
            if miro[nr][nc] == 3:
                return dist[curr_r][curr_c]
            
            # 거리 측정을 위해 Q에 추가될 때마다 +1
            Q.append((nr, nc))
            dist[nr][nc] = dist[curr_r][curr_c] + 1


T = int(input())
for tc in range(T):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    Q = []
    dist = [[0]*N for _ in range(N)]
    
    # 시작점을 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                answer = BFS(i, j)
    
    # 3으로 도달 못했을 경우
    if answer is None:
        print('#{} {}'.format(tc+1, 0))

    else:
        print('#{} {}'.format(tc+1, answer))



