import sys
sys.stdin = open('5178.txt', 'r')

T = int(input())
for tc in range(T):
    # 입력받기 #
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for m in range(M):
        idx, tree[idx] = map(int, input().split())
    # 입력받기 #

    # tree = [0, 0, 0, 3, 1 ,2] 인 상황
    # 1부터 N-M 을 채우기(값이 뒤에만 있으므로 역순으로 진행)
    for t in range(N-M, 0, -1):
        left = 2 * t
        right = 2 * t + 1
        if left <= N and right <= N:  # left, right 자식 idx가 모두 범위 내에 있을 때
            tree[t] = tree[left] + tree[right]
        else:  # left만 있을 경우(둘 다 없거나 right만 있는 경우는 없다.)
            tree[t] = tree[left]

    print("#{} {}".format(tc + 1, tree[L]))