for _ in range(1, 11):
    tc, N = map(int, input().split())
    num = list(map(int, input().split()))

    # 노드 연결 입력받기
    all_link = []
    for n in range(N * 2):
        if n % 2 == 0:
            link = [0] * 2
            link[0] = num[n]
            link[1] = num[n + 1]
            all_link.append(link)

    # 인접행렬 만들기
    num_link = [[0] * 100 for _ in range(100)]
    for i in range(len(all_link)):
        for j in range(1):
            num_link[all_link[i][j]][all_link[i][j + 1]] = 1

    # 기본 설정
    # 시작점이 담긴 stack과 check가 되어있지 않은 visit 리스트
    start = 0
    stack = []
    visit = [0] * 100
    stack.append(start)

    # len(stack)이 0이면
    # 1) 연결된 노드이면서 2) visit하지 않은 값이 없다는 뜻이므로
    # len(stack)이 0보다 클 때 진행
    while len(stack) > 0:
        go = stack.pop()
        if visit[go] == 'v':
            pass
        else:
            p = go
            visit[p] = 'v'
            for nb in range(100):
                if num_link[p][nb] == 1 and visit[nb] == 0:
                    stack.append(nb)
        if visit[99] == 'v':
            print("#{} {}".format(tc, 1))
            break
    if visit[99] != 'v':
        print("#{} {}".format(tc, 0))
