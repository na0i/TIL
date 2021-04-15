# import copy
#
arr = ['A', 'B', 'C', 'D']
N = len(arr)
# ans_1 = []
# ans_2 = []
#
#
# def perm(k):
#     if k == N:
#         print(arr)
#     else:
#         for i in range(k, N):
#             print(arr[k], arr[i], k, i)
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(k+1)
#             print(arr[k], arr[i], k, i)
#             arr[k], arr[i] = arr[i], arr[k]
#
#
# perm(0)
# print(ans_1)
# print(ans_2)
# # 깊은 복사 > 처음에 만들었던 객체와 복사된 객체가 전혀 달라지기 때문에 어느 한쪽을 수정한다고 해서 다른 한쪽이 영향 받는 일은 없다.
# # 방법 1
# temp_1 = arr[:]
# ans_1.append(temp_1)
#
# # 방법 2
# temp_2 = copy.deepcopy(arr)
# ans_2.append(temp_2)
#
#
for i in range(0, N):
    arr[0], arr[i] = arr[i], arr[0]
    for j in range(1, N):
        arr[1], arr[j] = arr[j], arr[1]
        for k in range(2, N):
            arr[2], arr[k] = arr[k], arr[2]
            print(arr)
            arr[2], arr[k] = arr[k], arr[2]
        arr[1], arr[j] = arr[j], arr[1]
    arr[0], arr[i] = arr[i], arr[0]
