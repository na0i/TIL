import sys
sys.stdin = open('5185.txt', 'r')

T = int(input())
for tc in range(T):
    N, num_16 = input().split()
    hex_to_bin = {'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    ans = []
    for i in range(int(N)):
        if num_16[i] in hex_to_bin:
            ans.append(hex_to_bin.get(num_16[i]))
        else:
            bin_num = ''
            for j in range(3, -1, -1):
                if int(num_16[i]) & (1 << j):
                    bin_num += '1'
                else:
                    bin_num += '0'
            ans.append(bin_num)

    str_ans = ''
    for k in range(len(ans)):
        str_ans += ans[k]

    print('#{} {}'.format(tc+1, str_ans))