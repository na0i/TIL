import sys
sys.stdin = open("farm.txt", "r")

T = int(input())
for tc in range(T):
    N = int(input())

    farm = []
    for _ in range(N):
        f = list(map(int, input()))
        farm.append(f)

    result = []

    for i in range(0, int(N / 2)+1):
        for j in range(int(N / 2) - i, int(N / 2) + i + 1):
            result.append(farm[i][j])

    for i in range(int(N / 2) + 1, N):
        for j in range(i - int(N/2), N - i + int(N/2)):
            result.append(farm[i][j])
    print('#{} {}'.format(tc+1, sum(result)))