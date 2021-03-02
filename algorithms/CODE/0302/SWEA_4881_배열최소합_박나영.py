T = int(input())
for tc in range(T):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    all_sero = []
    for i in range(N):
        sero = []
        for j in range(N):
            sero.append(nums[j][i])
        all_sero.append(sero)

    print(all_sero)
    arr = []
    check = [0] * N

    for i in range(N):
        arr[0] = all_sero[0][i]
        check[i] += 1