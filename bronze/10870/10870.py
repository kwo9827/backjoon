import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split()))
v = int(input())

count = 0

for i in range(len(arr)):
    if arr[i] == v:
        count += 1

print(count)