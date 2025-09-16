import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())

arr = list(map(int,input().split()))

for i in range(N):
    for j in range(0, N-i-1):
        if arr[j] < arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr[K-1])