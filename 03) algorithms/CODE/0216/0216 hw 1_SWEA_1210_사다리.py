for t in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 값이 2인 곳의 x 좌표 찾기
    for i in range(0, 100):
        if ladder[99][i] == 2:
            x_99floor = i

    x = x_99floor
    y = 99

    # 위로 올라가기
    while y > 0:
        if ladder[y][x - 1] == 1 and x - 1 >= 0:
            x -= 1
        # 왜 순서를 바꾸니까 pass일까?
        elif x + 1 <= 99 and ladder[y][x + 1] == 1:
            x += 1
        else:
            y -= 1
        ladder[y][x] = 0

    print('#{} {}'.format(tc, x))
