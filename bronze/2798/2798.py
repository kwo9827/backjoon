#2798 블랙잭
import sys
sys.stdin = open('input.txt')

def kfc(level,idx):
    global max_val
    if sum(path) > M:
        return

    if level == 3:
        if sum(path) > max_val:
            max_val = sum(path)
        return

    for i in range(idx, len(arr)):
        path.append(arr[i])
        kfc(level+1, i+1)
        path.pop()

N, M = map(int,input().split())
arr = list(map(int,input().split()))
path = []

max_val = 0

kfc(0,0)

print(max_val)
# ------------------------------------------------