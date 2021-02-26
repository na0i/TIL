import sys
sys.stdin = open("fish.txt","r")

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    g_time = list(map(int, input().split()))

    fishbread = [0] * 11112
    guest = [0] * 11112
    possible = [0] * 11112

    for i in range(M, 11112, M):
        for j in range(i, i + M):
            if j > 11111:
                pass
            else:
                fishbread[j] += K * (j // M)

    for j in range(N):
        guest[g_time[j]] += 1

    gsum = 0
    for k in range(11112):
        gsum += guest[k]
        possible[k] = fishbread[k] - gsum

    for l in range(11112):
        if possible[l] < 0:
            check = 'Impossible'
            break
        else:
            check = 'Possible'

    print('#{} {}'.format(tc + 1, check))
