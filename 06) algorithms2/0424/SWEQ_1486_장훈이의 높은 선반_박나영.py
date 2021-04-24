import sys
sys.stdin = open('1486.txt', 'r')


def top(person, psb_top):
    if psb_top >= B:
        result.append(psb_top)
        return


    if person < N:
        for h in range(N):
            if visit[h] == 0:
                visit[h] = 1
                top(person+1, psb_top + height[h])
                visit[h] = 0



T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    visit = [0] * N
    result = []

    top(0, 0)
    result.sort()
    print(result[0] - B)

    # 1 1
    # 2 4
    # 3 27
    # 4 11
    # 5 42
    # 6 32
    # 7 2
    # 8 3
    # 9 25
    # 10 0


