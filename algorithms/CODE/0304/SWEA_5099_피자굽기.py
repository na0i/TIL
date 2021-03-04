import sys
sys.stdin = open('pizza.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))

    hwaro = [0] * N
    idx_chz = [0] * M

    # (인덱스, 치즈양)
    for i in range(M):
        idx_chz[i] = (i+1, cheeze[i])

    # 일단 화로 개수만큼 피자 집어넣기(turn 1)
    for j in range(N):
        hwaro[j] = idx_chz[j]


    print(hwaro)
    print(idx_chz)