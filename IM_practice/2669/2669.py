# 2669 직사각형 네개의 합 면적 구하기
import sys
sys.stdin = open('input.txt')

lst = [[0] * 100 for _ in range(100)]

# x1,y1 왼쪽 아래 좌표    # x2,y2 오른쪽 위 좌표
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            lst[i][j] = 1
result = 0
for row in lst:
    result += sum(row)
print(result)

