T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    # 인접행렬 만들기
    matrix = []
    for _ in range(V+1):
        matrix.append(list([0]*(V+1)))

    # 인접행렬에 경로 추가하기
    for _ in range(E):
        s, e = map(int, input().split())
        matrix[s][e] = 1

    # 정점 시작과 끝 입력받기
    S, G = map(int, input().split())

    # 기본 설정
    # 시작점이 담긴 stack과 check가 되어있지 않은 visit 리스트
    stack = []
    visit = [0] * (V+1)
    go = S
    stack.append(go)

    # len(stack)이 0이면
    # 1) 연결된 노드이면서 2) visit하지 않은 값이 없다는 뜻이므로
    # len(stack)이 0보다 클 때 진행
    while len(stack) > 0:
        # stack 맨 위의 값 가지기
        go = stack.pop()
        # 갔던 곳이면 아무것도 하지 않고 그냥 넘어가기
        if visit[go] == 'v':
            continue
        else:
            # pop 해서 나온 값을 p로 지정
            p = go
            # 방문 체크
            visit[p] = 'v'
            ## print(stack)

            # p 행에 연결된 노드가 있는가
            for nb in range(V+1):
                if matrix[p][nb] == 1 and visit[nb] == 0:
                    stack.append(nb)
            ## print(visit)

    if visit[go] == 'v':
        print("#{} {}".format(tc + 1, 1))
    else:
        print("#{} {}".format(tc + 1, 0))
