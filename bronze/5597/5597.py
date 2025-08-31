import sys
sys.stdin = open('input.txt')

arr = [0] * 30

for i in range(28):
    N = int(input())
    arr[N-1] = N

for t in range(len(arr)):
    if arr[t] == 0:
        print(t+1)
