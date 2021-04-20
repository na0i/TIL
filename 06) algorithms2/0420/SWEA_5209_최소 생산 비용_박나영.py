import sys
sys.stdin = open('5209.txt', 'r')


def dfs(curr_r):    # curr_r: 현재 위치한 열
    global psb_cost, final_cost
    if psb_cost > final_cost:   # 가지치기(위치 중요)
        return

    if curr_r < N:
        for col in range(N):
            if visit[col] == 0:
                curr_c = col
                visit[curr_c] = 1
                psb_cost += cost[curr_r][curr_c]
                curr_r += 1    # row 하나씩 증가하며 col을 바꿔줄 예정
                dfs(curr_r)
                visit[curr_c] = 0
                curr_r -= 1
                psb_cost -= cost[curr_r][curr_c]

    if curr_r == N:
        final_cost = psb_cost
        return


T = int(input())
for tc in range(T):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    visit = [0] * N
    final_cost = 987654321
    psb_cost = 0    # psb_cost : possible cost(가능한 가격 후보)
    cnt = 0

    dfs(0)
    print('#{} {}'.format(tc+1, final_cost))