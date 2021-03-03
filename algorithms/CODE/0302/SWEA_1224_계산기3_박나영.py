import sys
sys.stdin = open('cal.txt', 'r')

for tc in range(10):
    N = int(input())
    zoongwui = list(input())
    # 연산자 리스트
    cal = ['(', ')', '+', '*']

    # 우선순위 딕셔너리
    in_s = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    out_s = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}

    stack_h = []
    hoowui = []

    # 중위를 후위로 바꾸기
    for i in range(len(zoongwui)):
        # 연산자가 아닐때 후위연산리스트에 추가
        if zoongwui[i] not in cal:
            hoowui.append(zoongwui[i])

        # 연산자라면
        else:
            # stack이 비어있을 땐 연산자 추가
            if len(stack_h) == 0:
                stack_h.append(zoongwui[i])
            # stack이 비어있지 않을 때
            else:
                # 닫힌 괄호라면
                if zoongwui[i] == ')':
                    # 열린 괄호가 나올 때까지 pop과 push 반복
                    # 열린 괄호 나오면 pop
                    while stack_h[-1] != '(':
                        p = stack_h.pop()
                        hoowui.append(p)
                    stack_h.pop()

                # stack-top 우선순위 < in-coming 우선순위라면
                # stack에 push
                elif len(stack_h) != 0 and in_s[stack_h[-1]] < out_s[zoongwui[i]]:
                    stack_h.append(zoongwui[i])

                # stack-top 우선순위 >= in-coming 우선순위라면
                # stack-top 우선순위 < in-coming 우선순위될 때까지
                # pop과 push 반복
                # 끝나면 stack에 push
                elif len(stack_h) != 0 and in_s[stack_h[-1]] >= out_s[zoongwui[i]]:
                    while in_s[stack_h[-1]] >= out_s[zoongwui[i]]:
                        hoowui.append(stack_h[-1])
                        stack_h.pop()
                    stack_h.append(zoongwui[i])

    # stack에 남은 것들 후위연산리스트에 추가
    if len(stack_h) != 0:
        for j in range(len(stack_h)-1, -1, -1):
            hoowui.append(stack_h[j])

    # 후위연산 계산하기
    stack_c = []
    for h in range(len(hoowui)):
        if hoowui[h] not in cal:
            stack_c.append(int(hoowui[h]))
        elif len(stack_c) > 1 and hoowui[h] == '+':
            plus = stack_c[-1] + stack_c[-2]
            stack_c.pop()
            stack_c.pop()
            stack_c.append(plus)
        elif len(stack_c) > 1 and hoowui[h] == '*':
            mul = stack_c[-2] * stack_c[-1]
            stack_c.pop()
            stack_c.pop()
            stack_c.append(mul)

    print('#{} {}'.format(tc+1, *stack_c))

