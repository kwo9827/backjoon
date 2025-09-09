import sys
sys.stdin = open('input.txt')

세로 = 5
arr = [list(input().strip()) for _ in range(세로)]

가로 = max(len(row) for row in arr)  # 가장 긴 줄의 길이

for i in range(가로):        # 열 기준
    for j in range(세로):    # 행 기준
        if i < len(arr[j]):  # 그 행에 i번째 글자가 있으면
            print(arr[j][i], end="")