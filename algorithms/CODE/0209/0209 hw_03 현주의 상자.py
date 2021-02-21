# 테스트케이스 개수 입력받기
# 박스상자 개수, 이름표 변경할 박스 개수 입력받기
T = int(input())
N, Q = map(int, input().split())


def hj_box():
    # 박스상자 개수만큼의 리스트 생성
    box = [0] * N

    # range(Q)가 아닌 range(1, Q+1)인 이유: q가 1부터 시작하기 위해
    # q는 1번째 실행할 때 1을 적고, 2번째 실행할때 2를 적으므로 ...
    # 즉 q = 몇번째 turn
    for q in range(1, Q+1):
        # 박스상자의 이름표를 수정할 범위 입력받기(l:왼쪽 ~ r:오른쪽)
        l, r = map(int, input().split())
        # range = r - l + 1(예시: 2부터 5까지면 2,3,4,5 이므로 5-2+1 = 4)
        # [r - i - 1] =  오른쪽부터 왼쪽으로 가며 숫자(q)로 바꾸기 시작(5-0-1, 5-1-1, 5-2-1 ... 5-4-1)
        for i in range(r - l + 1):
            box[r - i - 1] = q
    return box


for tc in range(T):
    print('#{}'.format(tc + 1), *hj_box())
