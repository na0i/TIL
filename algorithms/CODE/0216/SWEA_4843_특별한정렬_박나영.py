T = int(input())
for tc in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))

    # 버블정렬로 입력받은 num_list를 오름차순으로 정리
    def bubble_sort(num_list):
        for i in range(len(num_list)-1, 0, -1):
            for j in range(0, i):
                if num_list[j] > num_list[j+1]:
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
        return num_list

    sorted_num_list = bubble_sort(num_list)
    def special_list():
        special_sort = [0] * 10
        special_sort[0] = sorted_num_list[-1]
        special_sort[1] = sorted_num_list[0]
        special_sort[2] = sorted_num_list[-2]
        special_sort[3] = sorted_num_list[1]
        special_sort[4] = sorted_num_list[-3]
        special_sort[5] = sorted_num_list[2]
        special_sort[6] = sorted_num_list[-4]
        special_sort[7] = sorted_num_list[3]
        special_sort[8] = sorted_num_list[-5]
        special_sort[9] = sorted_num_list[4]
        return special_sort

    print('#{}'.format(tc+1), *special_list())

