def subtree_cnt(s):  # 중위순회하며 자식 노드 count
    global cnt
    if s:
        subtree_cnt(left[s])
        cnt += 1
        subtree_cnt(right[s])

T = int(input())
for tc in range(T):
    V, N = map(int, input().split())
    pa_ch = list(map(int, input().split()))

    pa = [0 for _ in range(V + 1)]
    left = [0 for _ in range(V + 1)]
    right = [0 for _ in range(V + 1)]

    for n in range(V-1):
        par = pa_ch[2*n]
        ch = pa_ch[2*n+1]
        if left[par] == 0:
            left[par] = ch
        else:
            right[par] = ch

    cnt = -1    # 시작 노드(부모)는 카운트하지 않기 위해
    subtree_cnt(N)

    print('#{} {}'.format(tc+1, cnt))