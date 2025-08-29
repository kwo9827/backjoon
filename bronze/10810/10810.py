import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())
arr = [0] * N
for i in range(M):
    i, j, k = map(int,input().split())
    for a in range(i-1, j):
        arr[a] = k

print(*arr)
