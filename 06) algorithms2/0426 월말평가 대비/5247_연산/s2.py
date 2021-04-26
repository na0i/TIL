# 2.
# memo 활용

# 연산을 위한 함수 생성
def calc(num, idx):
    if idx == 0:
        return num + 1
    elif idx == 1:
        return num - 1
    elif idx == 2:
        return num * 2
    else:
        return num - 10

def bfs():
    front = rear = -1
    rear += 1        # 초기값 -> enQueue 연산은 rear를 하나 증가 시키고 값을 넣음
    Q[rear] = (N, 0) # 0은 몇 번 연산을 했는지 누적하는 값
    memo[N] = 0

    while front != rear:

        front += 1                  # deQueue -> Queue에서 값을 가져오기 위해 1 증가
        cur_n, cur_cnt = Q[front]   # 현재 number, 현재 cnt를 Q에서 가져오기 (시작은 N, 0)

        if cur_n == M:              # 연산을 했는데 찾으려는 값 M면 그 값을 반환
            return cur_cnt

        for i in range(4):          # 아닐 경우 4가지 연산 수행
            next_n = calc(cur_n, i) # 다음 값 찾아서
            if 0 < next_n <= 1000000 and memo[next_n] == -1:  # 범위 안에 들어오는 연산이고(중간 연산 결과도 100만 이하)
                                                              # 아직 계산이 안되어 있다면(=> memo[next_n] == -1)

                memo[next_n] = memo[cur_n] + 1                # 값 계산하고
                rear += 1                                     # 다음 값을 받기 위해 증가 시키고
                Q[rear] = (next_n, cur_cnt+1)                 # 연산 횟수 누적 (cur_cnt+1)
    return memo[M]                                            # M에 있는 값 반환

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                          # N을 M으로 바꾸는 최소한의 연산 횟수(M은 100만 이하의 자연수)
    Q = [0] * 1000000
    memo = [-1] * 1000001                                     # 10000001? -> 1 ~ 100만까지 사용 가능
    print('#{} {}'.format(tc, bfs()))