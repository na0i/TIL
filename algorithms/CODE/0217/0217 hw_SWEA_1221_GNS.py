T = int(input())
for tc in range(T):
    t_num, length = input().split()
    galaxy = list(map(str, input().split()))

    ZERO = []
    ONE = []
    TWO = []
    THREE = []
    FOUR = []
    FIVE = []
    SIX = []
    SEVEN = []
    EIGHT = []
    NINE = []
    def galaxy_num_list():
        for g_num in range(len(galaxy)):
            if galaxy[g_num] == 'ZRO':
                ZERO.append(galaxy[g_num])
            elif galaxy[g_num] == 'ONE':
                ONE.append(galaxy[g_num])
            elif galaxy[g_num] == 'TWO':
                TWO.append(galaxy[g_num])
            elif galaxy[g_num] == 'THR':
                THREE.append(galaxy[g_num])
            elif galaxy[g_num] == 'FOR':
                FOUR.append(galaxy[g_num])
            elif galaxy[g_num] == 'FIV':
                FIVE.append(galaxy[g_num])
            elif galaxy[g_num] == 'SIX':
                SIX.append(galaxy[g_num])
            elif galaxy[g_num] == 'SVN':
                SEVEN.append(galaxy[g_num])
            elif galaxy[g_num] == 'EGT':
                EIGHT.append(galaxy[g_num])
            elif galaxy[g_num] == 'NIN':
                NINE.append(galaxy[g_num])
        return ZERO + ONE + TWO + THREE + FOUR + FIVE + SIX + SEVEN + EIGHT + NINE

    print('{}'.format(t_num))
    print(*galaxy_num_list())