T = int(input())
for tc in range(T):
    player_1st = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))


    def winner():
        # 만약 첫번째 플레이어가 A라면
        if player_1st == A:
            # i: A와 B 리스트의 인덱스
            # turn_a, b: a,b의 주사위 던진 횟수
            # a, b: 이동한 A,B의 위치
            i = 0
            turn_a = turn_b = 0
            a = b = 0
            # a, b가 보드(20) 안에 있고, 주사위 던진 횟수가 10 이하일 때
            while a < 20 and b < 20 and i < 10:
                a += A[i]
                turn_a += 1
                # a가 b를 잡으면
                if a == b:
                    b = 0

                b += B[i]
                turn_b += 1
                # b가 a를 잡으면
                if a == b:
                    a = 0

                # 주사위 둘다 굴렸으므로 인덱스 +1
                i += 1

                # a가 먼저 도착하면
                if a >= 20:
                    return 'A'
                    break
                # b가 먼저 도착하면
                elif b >= 20:
                    return 'B'
                    break
                # 주사위를 10회 굴렸는데도 a와 b 둘다 board 내에 있다면
                if turn_a == 10 and turn_b == 10 and a < 20 and b < 20:
                    return 'AB'
        # 첫번째 플레이어가 B라면
        else:
            i = 0
            turn_a = turn_b = 0
            a = b = 0
            while a < 20 and b < 20 and i < 10:
                b += B[i]
                turn_b += 1
                if a == b:
                    a = 0

                a += A[i]
                turn_a += 1

                i += 1

                if a == b:
                    b = 0

                if a >= 20:
                    return 'A'
                    break
                elif b >= 20:
                    return 'B'
                    break
                if turn_a == 10 and turn_b == 10 and a < 20 and b < 20:
                    return 'AB'

    print('#{} {}'.format(tc+1, winner()))