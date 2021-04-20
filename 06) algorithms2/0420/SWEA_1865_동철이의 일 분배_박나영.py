import sys
sys.stdin = open('1865.txt', 'r')


def dfs(curr_r):
    global psb_per, final_per
    if psb_per < final_per:    # 가지치기
        return

    if curr_r < N:
        for col in range(N):
            if visit[col] == 0:
                curr_c = col
                if work[curr_r][curr_c] != 0:    # 0인 경우 제외('주어진 일을 모두 성공' 이라는 조건)
                    visit[curr_c] = 1
                    psb_per *= work[curr_r][curr_c]
                    curr_r += 1
                    dfs(curr_r)
                    visit[curr_c] = 0
                    curr_r -= 1
                    psb_per /= work[curr_r][curr_c]

    if curr_r == N:
        final_per = psb_per
        return


T = int(input())
for tc in range(T):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]

    visit = [0] * N
    final_per = -987654321
    psb_per = 1

    for i in range(N):
        for j in range(N):
            work[i][j] = round(work[i][j] * 0.01, 2)

    dfs(0)
    print('#{} {:6f}'.format(tc+1, float(final_per*100)))    # 소수점 뒤 6자리에서 끊기