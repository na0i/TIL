import sys
sys.stdin = open('input.txt', 'r')


# 중위 순회
def zw_sh(T):
    if T:
        zw_sh(int(left[T])) # 왼쪽
        print(word[T], end='') # V
        zw_sh(int(right[T])) # 오른쪽


for tc in range(10):
    # 정점 개수 입력 받기
    N = int(input())
    # 노드 정보 입력 받기
    all_node = []
    for n in range(N):
        all_node.append(list(input().split()))

    # ['4', 'O', '8', '0'], ['5', 'T', '0', '0'], ['6', 'A', '0', '0']과 같이 뒤에 0 채워주기
    for i in range(N):
        if len(all_node[i]) != 4:
            all_node[i] += ['0'] * (4 - len(all_node[i]))

    word = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    for j in range(N):
        word[j+1] = all_node[j][1]
        left[j+1] = all_node[j][2]
        right[j+1] = all_node[j][3]

    print("#{} ".format(tc + 1), end='')
    zw_sh(1)
    print()