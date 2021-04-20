import sys
sys.stdin = open('5207.txt', 'r')


def bin_search(lst, l, r, key):
    bf_check = None
    while l <= r:
        mid = (l+r) // 2
        if lst[mid] == key:
            result.append(key)
            break
        elif lst[mid] < key:
            l = mid + 1
            curr_check = 'left'
        elif lst[mid] > key:
            r = mid - 1
            curr_check = 'right'
        if bf_check == curr_check:
            break
        bf_check = curr_check


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    N_list = sorted(list(map(int, input().split())))
    M_list = sorted(list(map(int, input().split())))

    result = []

    for k in range(M):
        bin_search(N_list, 0, N-1, M_list[k])

    print('#{} {}'.format(tc+1, len(result)))