import sys
sys.stdin = open('1210.txt', 'r')

for tc in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 출발 지점 찾기 #
    for c in range(100):
        if ladder[99][c] == 2:
            start_r = 99
            start_c = c

    curr_r = 99
    curr_c = start_c

    # 위로 올라가기 #
    while curr_r >= 0:
        # 윗칸이 1인 경우
        if ladder[curr_r-1][curr_c] == 1:
            next_r = curr_r - 1  # 한칸 위로 올라가기
            next_c = curr_c

            if 0 <= next_c-1 <= 99 and ladder[next_r][next_c-1] == 1:  # 올라갔는데 왼쪽이 1이면 왼쪽으로 이동
                while 0 <= next_c-1 <= 99 and ladder[next_r][next_c-1] == 1:
                    next_c = next_c - 1
                # 이동한 좌표로 현재 좌표 수정
                curr_r = next_r
                curr_c = next_c

            elif 0 <= next_c+1 <= 99 and ladder[next_r][next_c+1] == 1:  # 올라갔는데 오른쪽이 1이면 오른쪽으로 이동
                while 0 <= next_c+1 <= 99 and ladder[next_r][next_c+1] == 1:
                    next_c = next_c + 1
                # 이동한 좌표로 현재 좌표 수정
                curr_r = next_r
                curr_c = next_c

            # if와 elif 문에 걸리지 않았을 경우를 위해
            # 현재 좌표 = 이동해온 좌표
            curr_r = next_r
            curr_c = next_c

        # 0번째 줄에 도착했다면 종료
        if curr_r == 0:
            print('#{} {}'.format(tc, curr_c))
