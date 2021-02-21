T = int(input())
for tc in range(T):
	N, M = map(int, input().split())
	num_1 = list(map(int, input().split()))
	num_2 = list(map(int, input().split()))

	if N <= M:
		mul_sum_list = []
		for i in range(M - N + 1):
			mul_sum = 0
			for j in range(N):
				mul_sum += num_1[j] * num_2[i+j]
			mul_sum_list.append(mul_sum)

	else:
		mul_sum_list = []
		for i in range(N - M + 1):
			mul_sum = 0
			for j in range(M):
				mul_sum += num_1[i+j] * num_2[j]
			mul_sum_list.append(mul_sum)


	print('#{} {}'.format(tc+1, max(mul_sum_list)))