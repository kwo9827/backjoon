import sys
sys.stdin = open('input.txt')

arr = [list(map(int,input().split())) for _ in range(9)]

max_num = arr[0][0]
a = 1
b = 1

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num:
            max_num = arr[i][j]
            a = i + 1
            b = j + 1

print(max_num)
print(a, b)




