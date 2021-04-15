import sys
sys.stdin = open('5189.txt', 'r')


def dfs(v):
    global cnt, battery, test_battery
    if battery > test_battery:
        return

    if cnt == N:
        battery += golf[v][1]
        test_battery = battery
        return

    for w in range(N+1):
        if visit[w] == 0 and golf[v][w] != 0:
            cnt += 1
            battery += golf[v][w]
            visit[w] = 1
            dfs(w)
            visit[w] = 0
            battery -= golf[v][w]


T = int(input())
for tc in range(T):
    N = int(input())
    golf = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    # visit = [[0 for _ in range(N)] for _ in range(N)]
    visit = [0] * (N+1)
    cnt = 1
    battery = 0
    test_battery = 987654321

    print(golf)
    visit[1] = 1
    dfs(1)
    print(test_battery)
