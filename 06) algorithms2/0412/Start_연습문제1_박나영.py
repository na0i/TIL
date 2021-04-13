num = '0000000111100000011000000111100110000110000111100111100111111001100111'
cut_num = []

for i in range(0, len(num), 7):
    n = num[i:i+7]
    cut_num.append(n)

res = []
for j in range(len(cut_num)):
    ans = 0
    for k in range(7):
       ans += int(cut_num[j][k]) * (2**(6-k))
    res.append(ans)


print(cut_num)
# ['0000000', '1111000', '0001100', '0000111', '1001100', '0011000', '0111100', '1111001', '1111100', '1100111']
print(res)
# [0, 120, 12, 7, 76, 24, 60, 121, 124, 103]