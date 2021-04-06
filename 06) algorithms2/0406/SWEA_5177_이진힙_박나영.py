import sys
sys.stdin = open('5177.txt', 'r')

# A: 원래 입력받은 NUM 리스트(7 2 5 3 4 6)
# B: 새로 정렬될 이진힙 리스트(2 3 5 7 4 6)
def change(A, B, i):
    while i >= 1:  # 반복 조건 설정
        if B[i] < B[i // 2]:  # 부모노드가 자식노드보다 크다면 변경
            temp = B[i]
            B[i] = B[i//2]
            B[i//2] = temp
        i = i // 2  # 그 위의 부모노드와 자식노드도 똑같이 변경

T = int(input())
for tc in range(T):
    N = int(input())
    nums = [0] + list(map(int, input().split()))

    b_heap = [0] * (N+1)  # 이진힙 정렬할 리스트 생성
    b_heap[1] = nums[1]  # idx 0의 값과 바꾸지 않도록 1은 따로 지정

    for i in range(2, N+1):
        b_heap[i] = nums[i]  # 일단 이진힙에 입력 num을 넣어준다.
        change(nums, b_heap, i)

    pa_idx = []  # 마지막 노드의 부모 idx를 찾을 리스트 생성
    while N > 1:  # N >= 1이면 0도 들어감
        pa_idx.append(N // 2)
        N = N // 2  # N이 8이라면 4, 2, 1이 들어감

    ans = 0
    for i in range(len(pa_idx)):
        ans += b_heap[pa_idx[i]]  # 이진힙[마지막 노드의 부모 idx]의 합

    print("#{} {}".format(tc+1, ans))

