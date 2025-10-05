import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))

mn = arr[0]
mx = arr[0]

for i in range(1, n):
    if arr[i] < mn:
        mn = arr[i]
    if arr[i] > mx:
        mx = arr[i]

print(mn * mx)