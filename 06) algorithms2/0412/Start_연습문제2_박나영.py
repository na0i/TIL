input_num = '01D06079861D79F99F'
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
# ['0000', '0001', '1101', '0000', '0110', '0000', '0111', '1001', '1000', '0110', '0001', '1101', '0111', '1001', '1111', '1001', '1001', '1111']
# -- 16진수 → 2진수 -- #

# -- 2진수 이어 붙이기 -- #
num_str = ''
for j in range(len(res)):
    num_str += res[j]

print(num_str)
# 000000011101000001100000011110011000011000011101011110011111100110011111
# -- 2진수 이어 붙이기 -- #

# -- 2진수 7개씩 자르기 -- #
cut_num = []

for i in range(0, len(num_str), 7):
    n = num_str[i:i+7]
    cut_num.append(n)
print(cut_num)
# -- 2진수 7개씩 자르기 -- #

# -- 잘린 2진수 10진수로 변환 -- #
num_to_10 = []
for j in range(len(cut_num)):
    ans2 = 0
    for k in range(len(cut_num[j])):
       ans2 += int(cut_num[j][k]) * (2**(6-k))
    num_to_10.append(ans2)

print(num_to_10)
# [0, 116, 12, 7, 76, 24, 58, 121, 124, 103, 96]
# -- 잘린 2진수 10진수로 변환 -- #