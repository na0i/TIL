T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    # 버스정류장 리스트 생성
    # 0부터 N까지의 버스정류장이므로 N+1개의 버스정류장 필요
    bus_stop = [0] * (N+1)
    # 충전소 위치를 1로 check
    for i in range(M):
        bus_stop[charge[i]] += 1

    def electric_bus():
        # b = 현위치, cnt = turn 횟수
        b = 0
        cnt = 0
        # 현위치가 버스정류장 길이보다 작을 때 반복
        while b < N:
            # 현위치 = 이전위치 + 한번 가는 거리
            b += K
            # 만약 현위치가 N보다 크면 cnt 반환
            # 아니라면 그대로 진행하며 cnt에 +1
            if b >= N:
                break
            cnt += 1

            # 만약 충전소에 도착했다면 그대로 진행
            if bus_stop[b] == 1:
                continue

            # 도착한 곳이 충전소가 아니라면
            else:
                # 심지어 돌아갈 곳에 충전소가 없다면 0 반환
                j_sum = 0
                for j in range(b-K+1, b):
                    j_sum += bus_stop[j]
                if j_sum == 0:
                    return 0

                # [이전위치] ~ [현위치-1] 정류장에 돌아갈 충전소가 있다면 그곳으로 인덱스 바꾸기
                else:
                    for j in range(b-K+1, b):
                        if bus_stop[j] == 1:
                            b = j

        return cnt

    print('#{} {}'.format(tc+1, electric_bus()))