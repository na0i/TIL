import sys
sys.stdin = open('10726.txt', 'r')


def to_bin(n):
    ans = ''
    for i in range(99, -1, -1):
        if n & (1 << i):
            ans += '1'
        else:
            ans += '0'
    return ans


def on_off(strr, n):
    if strr[100-n:101] == '1' * n:
        return 'ON'
    else:
        return 'OFF'


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc+1, on_off(to_bin(M), N)))


