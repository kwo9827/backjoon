arr = [list(map(int, input().split())) for _ in range(5)]
lst = []
for _ in range(5):
    lst1 = list(map(int, input().split()))
    lst.extend(lst1)   # 불러주는 번호

bingo = 0

for i in range(len(lst)):

    for x in range(5):
        for y in range(5):
            if arr[x][y] == lst[i]:
                arr[x][y] = 0

    bingo = 0

    for r in range(5): # 가로줄
        count = 0
        for c in range(5):
            if arr[r][c] == 0:
                count += 1
        if count == 5:
            bingo += 1

    for c in range(5):  # 세로줄
        count = 0
        for r in range(5):
            if arr[r][c] == 0:
                count += 1
        if count == 5:
            bingo += 1


    count = 0
    for r in range(5):   # 왼쪽 대각선
        if arr[r][r] == 0:
            count += 1
    if count == 5:
        bingo += 1


    count = 0
    for r in range(5):  # 오른쪽 대각선
        if arr[r][4 - r] == 0:
            count += 1
    if count == 5:
        bingo += 1

    if bingo >= 3:
        print(i + 1)
        break
