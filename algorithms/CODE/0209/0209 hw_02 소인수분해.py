T = int(input())


# 소인수 분해 함수 정의 - 숫자 입력
def prime_number(num):
    # 2, 3, 5, 7, 9의 지수 개수를 담기 위해 길이가 5인 리스트 생성
    abcde = [0] * 5
    # 소수 목록
    p_n = [2, 3, 5, 7, 11]
    # num을 소인수로 나누기 반복
    while num > 1:
        # idx는 0부터 4까지
        for idx in range(len(abcde)):
            # 만약 num이 p_n의 소수로 나누어진다면
            if num % p_n[idx] == 0:
                # 같은 인덱스의 지수개수 리스트에 +1
                abcde[idx] += 1
                num = num / p_n[idx]

    return abcde


for tc in range(T):
    N = int(input())
    print("#{} {} {} {} {} {}".format(tc + 1, prime_number(N)[0], prime_number(N)[1], prime_number(N)[2], prime_number(N)[3], prime_number(N)[4]))
