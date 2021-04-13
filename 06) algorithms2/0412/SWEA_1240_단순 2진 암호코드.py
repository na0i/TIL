import sys
sys.stdin = open('1240.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    code = [list(input()) for _ in range(N)]

    pw_pattern = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4', '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

    for i in range(N):
        j = len(code[i])
        while j > 0:
            j -= 1
            if code[i][j] == '1':
                pw_code = code[i][0:j+1]
                break
    str_pw = ''
    for i in range(len(pw_code)):
        str_pw += pw_code[i]

    # print(str_pw)

    pw_list = []
    k = len(str_pw)
    while k > 0:
        k -= 1
        if str_pw[k] == '1' and pw_pattern.get(str_pw[k - 6 : k + 1]):
            pw_list.append(pw_pattern.get(str_pw[k - 6 : k + 1]))
            k -= 6

    pw_list.reverse()
    # print(pw_list)

    test_1 = (int(pw_list[0]) + int(pw_list[2]) + int(pw_list[4]) + int(pw_list[6]))*3 + (int(pw_list[1]) + int(pw_list[3]) + int(pw_list[5]))
    test_2 = test_1 + int(pw_list[7])
    pw_list_sum = int(pw_list[0]) + int(pw_list[2]) + int(pw_list[4]) + int(pw_list[6]) + int(pw_list[1]) + int(pw_list[3]) + int(pw_list[5]) + int(pw_list[7])
    if test_2 % 10 == 0:
        print('#{} {}'.format(tc+1, pw_list_sum))
    else:
        print('#{} {}'.format(tc+1, '0'))

