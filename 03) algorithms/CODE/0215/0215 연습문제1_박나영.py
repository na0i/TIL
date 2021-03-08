N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input().split()))

# 원소당 이웃하는 리스트를 총괄해 담을 빈 리스트 생성
neighbor_list = []
# 5 * 5 행렬이므로 범위는 i와 j 둘다 5
# i, j는 원소 위치
for i in range(5):
    for j in range(5):
        # 상하좌우에 따른 delta 값 리스트
        # dr: 행 기준 상하좌우
        # dc: 열 기준 상하좌우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        # 상하좌우 이웃을 담을 빈 리스트 생성
        k_neighbor = []
        # 상하좌우이므로 범위는 4
        for k in range(4):
            # 원래 위치인 i,j에 delta를 더한 값이 0~5 이내일 때 수행
            # i + dr[k] = 새로운 위치의 행 값
            # j + dc[k] = 새로운 위치의 열 값
            if 0 <= i+dr[k] < 5 and 0 <= j+dc[k] < 5:
                # '새로운 위치 - 원래 위치'의 절댓값
                abs_num = abs(arr[i+dr[k]][j+dc[k]] - arr[i][j])
                # 이웃 리스트에 추가
                k_neighbor.append(abs_num)
            # 원소당 이웃들 리스트를 총합
            neighbor_list.append(k_neighbor)

# 리스트 내의 리스트 순회하며 총합 구하기
total = 0
for li in range(len(neighbor_list)):
    for n in range(len(neighbor_list[li])):
        total += neighbor_list[li][n]

print(total)