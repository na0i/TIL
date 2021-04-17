import sys
sys.stdin = open('4366.txt', 'r')


def to_str(lst):
    num_list = []
    for k in range(len(lst)):
        num_str = ''
        for l in range(len(lst[k])):
            num_str += lst[k][l]
        num_list.append(num_str)
    return num_list


def bi_to_dex(strr):
    bi_dex = 0
    for s in range(len(strr)-1, -1, -1):
        if strr[s] == '1':
            bi_dex += 2 ** (len(strr) - s - 1)
        else:
            continue
    return bi_dex


def tr_to_dex(strr):
    tr_dex = 0
    for s in range(len(strr)-1, -1, -1):
        tr_dex += int(strr[s]) * (3 ** (len(strr) - s - 1))
    return tr_dex


T = int(input())
for tc in range(T):
    bi_num = list(input())
    tr_num = list(input())

    psb_bi_num = []
    for i in range(len(bi_num)):
        temp_bi = bi_num[:]
        if bi_num[i] == '1':
            temp_bi[i] = '0'
            psb_bi_num.append(temp_bi)
        else:
            temp_bi[i] = '1'
            psb_bi_num.append(temp_bi)

    psb_tr_num = []
    for j in range(len(tr_num)):
        temp_tr_1 = tr_num[:]
        temp_tr_2 = tr_num[:]
        if tr_num[j] == '0':
            temp_tr_1[j] = '1'
            psb_tr_num.append(temp_tr_1)
            temp_tr_2[j] = '2'
            psb_tr_num.append(temp_tr_2)
        elif tr_num[j] == '1':
            temp_tr_1[j] = '0'
            psb_tr_num.append(temp_tr_1)
            temp_tr_2[j] = '2'
            psb_tr_num.append(temp_tr_2)
        elif tr_num[j] == '2':
            temp_tr_1[j] = '0'
            psb_tr_num.append(temp_tr_1)
            temp_tr_2[j] = '1'
            psb_tr_num.append(temp_tr_2)

    psb_dex_1 = []
    for i in range(len(psb_bi_num)):
        psb_dex_1.append(bi_to_dex(psb_bi_num[i]))

    psb_dex_2 = []
    for j in range(len(psb_tr_num)):
        psb_dex_2.append(tr_to_dex(psb_tr_num[j]))

    for k in range(len(psb_dex_1)):
        if psb_dex_1[k] in psb_dex_2:
            print('#{} {}'.format(tc+1, psb_dex_1[k]))