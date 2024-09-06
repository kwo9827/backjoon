#2953 나는 요리사다.
import sys
sys.stdin = open('input.txt')

arr = [list(map(int,input().split())) for _ in range(5)]

max_val = 0
max_idx = -1

for r in range(5):
    sum_val = 0
    for c in range(4):
        sum_val += arr[r][c]

    if sum_val > max_val:
        max_val = sum_val
        max_idx = r

print(f'{max_idx+1} {max_val}')
