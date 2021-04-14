import sys
sys.stdin = open('5186.txt', 'r')


# 0 ~ 1 사이 소수 2진 변환
def to_bin():
    global f_num
    a = f_num

    while len(bin_num) < 13:    # 13자리가 넘어가면 overflow
        a *= 2    # 0.625 * 2 = 1.25
        b = str(a)
        if a > 1:
            bin_num.append(1)
            b = '0.' + b[2:]    # b = 0. + 25
            a = float(b)    # b를 숫자 type 으로 변환
        elif a < 1:
            bin_num.append(0)
            b = '0.' + b[2:]
            a = float(b)
        elif a == 1.0:    # a가 1이면 2진수 변환 끝
            bin_num.append(1)
            break


T = int(input())
for tc in range(T):
    f_num = float(input())
    bin_num = []
    to_bin()

    # 문자열 형태로 출력 #
    ans = ''
    for i in range(len(bin_num)):
        ans += str(bin_num[i])

    if len(bin_num) == 13:
        print('#{} {}'.format(tc+1, 'overflow'))
    else:
        print('#{} {}'.format(tc+1, ans))
