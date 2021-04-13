input_num = '0269FAC9A0'
num_10 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num_16 = {'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

# -- 16진수 → 2진수 -- #
res = []
for i in range(len(input_num)):
    ans = ''
    cnt = 0
    if input_num[i] in num_10:
        trans_n = int(input_num[i])
        while cnt < 4:
            ans += str(trans_n % 2)
            cnt += 1
            trans_n //= 2
        res.append(ans[::-1])
    else:
        ans = num_16.get(input_num[i])
        res.append(ans)

print(res)
# ['0000', '0010', '0110', '1001', '1111', '1010', '1100', '1001', '1010', '0000']
# -- 16진수 → 2진수 -- #

# -- 2진수 이어 붙이기 -- #
num_str = ''
for j in range(len(res)):
    num_str += res[j]

print(num_str)
# 0000001001101001111110101100100110100000
# -- 2진수 이어 붙이기 -- #

# -- 암호 비트 패턴 -- #
pw_pattern = {'001101': '0', '010011': '1', '111011': '2', '110001': '3', '100011': '4', '110111': '5', '001011': '6', '111101': '7', '011001': '8', '101111': '9'}
# -- 암호 비트 패턴 -- #

# -- 2진수 속 암호 찾기 -- #
pw_list = []
k = len(num_str)
while k > 0:
    k -= 1
    if num_str[k] == '1' and pw_pattern.get(num_str[k-5:k+1]):
        pw_list.append(pw_pattern.get(num_str[k-5:k+1]))
        k -= 5

pw_list.reverse()
print(pw_list)
# ['1', '1', '7', '8', '0']
# -- 2진수 속 암호 찾기 -- #
