# 테스트 케이스 4개
for t in range(4):
    N = int(input())
    g = list(map(int, input().split()))

    # gravity 함수 정의하기
    # 돌렸을 때 낙하가 제일 큰 곳? =  정사각형 한 변 길이 - 가장 높은 곳의 개수
    def gravity(N, g):
        # 가장 높은 곳 찾기
        max_g = g[0]
        for i in range(len(g)):
            if max_g <= g[i]:
                max_g = g[i]

        # 높은 곳과 동일한 높이 개수 세기
        count = 0
        for j in range(len(g)):
            if g[j] == max_g:
                count += 1

        result = N - count
        return result

    print(gravity(N, g))