T = int(input())


def subtree(N):
    if N != 0:
        sub_count.append('V')
        subtree(left[N])
        subtree(right[N])

    return len(sub_count)


for tc in range(T):
    E, N = map(int, input().split())
    pa_ch = list(map(int, input().split()))

    sub_count = []
    left = [0] * (E+2)
    right = [0] * (E+2)

    for p in range(E):
        pa, ch = pa_ch[p*2], pa_ch[p*2+1]
        if left[pa] == 0:
            left[pa] = ch
        else:
            right[pa] = ch

    print("#{} {}".format(tc+1, subtree(N)))