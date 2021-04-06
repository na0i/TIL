import sys
sys.stdin = open('bst.txt', 'r')

T = int(input())


# count = 1
# 여기 두면 tc 돌고나서도 1의 리셋이 안된다.
def make_bst(n):
    # count = 1
    # 이러면 재귀 호출때마다 count가 1로 reset 되기 때문에 주의하자!
    global count

    if n <= N:
        make_bst(2*n)
        tree[n] = count
        count += 1
        make_bst(2*n+1)

    return tree


for tc in range(T):
    N = int(input())
    tree = [0] * (N+1)
    count = 1  # for문 안에 있어야 tc 한번 끝날때마다 1이 됨

    make_bst(1)  # 만든 이진탐색트리 불러오기
    print('#{} {} {}'.format(tc+1, tree[1], tree[N//2]))