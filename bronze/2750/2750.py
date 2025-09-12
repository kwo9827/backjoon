import sys
sys.stdin = open('input.txt')

N = int(input())

arr = []

for _ in range(N):
    a= int(input())

    arr.append(a)

for i in range(len(arr)):
    for j in range(0, N-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

for x in arr:
    print(x)
