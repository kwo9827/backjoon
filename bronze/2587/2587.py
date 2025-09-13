import sys
sys.stdin = open('input.txt')

arr = []

for _ in range(5):
    N = int(input())

    arr.append(N)

for i in range(5):
    for j in range(0, 5-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(sum(arr)//5)
print(arr[5//2])
