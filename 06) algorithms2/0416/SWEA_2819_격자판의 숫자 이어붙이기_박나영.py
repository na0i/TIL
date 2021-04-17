import sys
sys.stdin = open('2819.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(curr_r, curr_c):
    global cnt
    for d in range(4):
        nr = curr_r + dr[d]
        nc = curr_c + dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            num.append(str(grid[nr][nc]))
            cnt += 1
            dfs(nr, nc)
            cnt -= 1
            num.remove(str(grid[nr][nc]))
        else:
            continue
        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
            return

    if cnt > 6:
        return

T = int(input())
for tc in range(T):
    grid = [list(map(int, input().split())) for _ in range(4)]

    cnt = 1
    num = []
    print(grid)

    print(dfs(0, 0))
    print(num)