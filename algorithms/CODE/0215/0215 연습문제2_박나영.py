arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)

section_list = []
for i in range(1<<10):
    section = []
    for j in range(n+1):
        if i & (1<<j):
            section.append(arr[j])
    section_list.append(section)

for k in range(len(section_list)):
    s_total = 0
    for l in range(len(section_list[k])):
        s_total += section_list[k][l]
    # 들여쓰기를 for문 내에 하지 않는 것 check!
    if s_total == 10:
        print(section_list[k])