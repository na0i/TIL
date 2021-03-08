T = int(input())
for tc in range(T):
    N = int(input())

    all_arr = []
    for i in range(N):
        arr = [1] * (i+1)
        all_arr.append(arr)

    for i in range(2, N):
        for j in range(1, i):
            all_arr[i][j] = all_arr[i-1][j] + all_arr[i-1][j-1]

    print('#{}'.format(tc+1))
    for i in range(N):
        for j in range(len(all_arr[i])):
            print(all_arr[i])