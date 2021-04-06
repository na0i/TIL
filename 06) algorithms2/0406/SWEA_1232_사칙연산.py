import sys
sys.stdin = open('1232.txt', 'r')

for tc in range(10):
    N = int(input())

    # -- 노드 정보 입력 받기 -- #
    all_nodes = []
    for n in range(N):
        node_info = list(input().split())
        all_nodes.append(node_info)

    for i in range(N):
        if len(all_nodes[i]) != 4:
            all_nodes[i] += ['0'] * (4 - len(all_nodes[i]))
    # -- 노드 정보 입력 받기 -- #

    # -- 노드 정보 저장 -- #
    cal = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    result = [0] * (N+1)

    for j in range(N):
        cal[j+1] = all_nodes[j][1]
        left[j+1] = all_nodes[j][2]
        right[j+1] = all_nodes[j][3]
    # -- 노드 정보 저장 -- #

    for k in range(N, 1, -1):
        stack = []
        if left[k] != '0' and right[k] != '0':
            stack.append(cal[int(left[k])])
            stack.append(cal[int(right[k])])
            # print(stack)
            # print(cal[k])
            if cal[k] == '+':
                cal[k] = int(stack[0]) + int(stack[1])
            elif cal[k] == '-':
                cal[k] = int(stack[0]) - int(stack[1])
            elif cal[k] == '*':
                cal[k] = int(stack[0]) * int(stack[1])
            elif cal[k] == '/':
                cal[k] = int(stack[0]) / int(stack[1])

    if cal[1] == '+':
        cal[1] = int(cal[2]) + int(cal[3])
    elif cal[1] == '-':
        cal[1] = int(cal[2]) - int(cal[3])
    elif cal[1] == '*':
        cal[1] = int(cal[2]) * int(cal[3])
    elif cal[1] == '/':
        cal[1] = int(cal[2]) / int(cal[3])

    print('#{} {}'.format(tc+1, int(cal[1])))

