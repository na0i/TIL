arr = [1, 2, 3]
N = 3
sel = [0] * 3


def powerset(idx):
    if idx == N:
        print(sel)

    else:
        for i in range(1, N+1):
            sel[idx] = i
            powerset(idx+1)

powerset(0)