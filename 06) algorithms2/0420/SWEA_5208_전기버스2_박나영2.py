import sys
sys.stdin = open('5208.txt', 'r')


def dfs():
    pass


T = int(input())
for tc in range(T):
    info = list(map(int, input().split()))

    destination = info[0]
    stop = [0] + info[1:]    # idx 맞춰주기 위해 앞에 + [0]

