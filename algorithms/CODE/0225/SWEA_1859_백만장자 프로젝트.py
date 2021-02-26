import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(T):
    N = int(input())
    daily_p = list(map(int, input().split()))

    buy = 0
    sell = 0
    max_p = daily_p[-1]
    for i in range(N-1, -1, -1):
        if daily_p[i] < max_p:
            buy += daily_p[i]
            sell += max_p
        elif daily_p[i] >= max_p:
            max_p = daily_p[i]

    print('#{}'.format(tc+1), end = ' ')
    print(sell - buy)