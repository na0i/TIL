T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    trees = [0] * N
    for _ in range(N):
        trees[_] = list(map(int, input().split()))

    # 정원의 크기 : N * M
    garden = list([0] * M for g in range(N))

    # 입력받은 나무들로 정원리스트 만들기
    for j in range(M):
        for i in range(N):
            garden[i][j] = trees[i][j]

    # 심은 나무의 수
    planting = []
    for j in range(M):
        if j % 2 == 0:
            for i in range(N):
                planting.append(garden[i][j])

    # 나무 심기 총 비용
    cost = 0
    for j in range(M):
        if j % 2 == 0:
            for i in range(N):
                cost += garden[i][j]

    # 가장 비싼 나무의 가격
    cost_max = 0
    idx = -1
    for j in range(M):
        if j % 2 == 0:
            for i in range(N):
                if garden[i][j] >= cost_max:
                    cost_max = garden[i][j]
                    if j > idx:
                        idx= j

    print('#{} {} {} {} {}'.format(tc+1, cost, len(planting), cost_max, idx+1))

