def sum_list(arr):
	total = 0
	for i in range(len(arr)):
		total += arr[i]
	return total

def two_rows_num():
	if n <= m:
		group_mul = []
		for i in range(m-n+1):
			mul_list = []
			group_mul.append(mul_list)
			for j in range(n):
				mul = n_list[j] * m_list[i+j]
				mul_list.append(mul)
	else:
		group_mul = []
		for i in range(n-m+1):
			mul_list = []
			group_mul.append(mul_list)
			for j in range(m):
				mul = n_list[i+j] * m_list[j]
				mul_list.append(mul)

	group_total = []
	for gm_idx in range(len(group_mul)):
		s_m = sum_list(group_mul[gm_idx])
		group_total.append(s_m)

	max_mul_total = 0
	for idx in range(len(group_total)):
		if group_total[idx] > max_mul_total:
			max_mul_total = group_total[idx]

	return max_mul_total

T = int(input())
for tc in range(T):
	n, m = map(int, input().split())
	n_list = list(map(int, input().split()))
	m_list = list(map(int, input().split()))
	print('#{} {}'.format(tc+1, two_rows_num()))