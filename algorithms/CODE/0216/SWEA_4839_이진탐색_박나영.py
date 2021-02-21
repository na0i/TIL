# 테스트 케이스 개수 입력
T = int(input())
for tc in range(T):
    # [페이지수, A가 찾을 페이지, B가 찾을 페이지] 입력받기
    P = list(map(int, input().split()))
    # 이진탐색 함수 만들기
    def bin_search(Num):
        start = 1
        end = P[0]
        cnt = 1

        while start <= end:
            middle = (start + end) // 2
            if Num == middle:
                return cnt
            elif Num < middle:
                end = middle
                cnt += 1
            elif Num > middle:
                start = middle
                cnt += 1

    # A와 B의 turn 횟수를 비교하여 작은 쪽이 승리, 비겼을 때 0 print
    if bin_search(P[1]) > bin_search(P[2]):
        print('#{} {}'.format(tc + 1, 'B'))
    elif bin_search(P[1]) < bin_search(P[2]):
        print('#{} {}'.format(tc + 1, 'A'))
    elif bin_search(P[1]) == bin_search(P[2]):
        print('#{} {}'.format(tc + 1, 0))