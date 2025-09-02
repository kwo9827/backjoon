import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

arr=[]

for t in range(N):
    arr.append(t+1)

# for _ in range(M):
#     i, j = map(int,input().split())
#     arr[i-1:j] = arr[i-1:j][::-1]

for _ in range(M):
    i, j = map(int,input().split())
    l, r = i-1, j-1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l = l + 1
        r = r - 1

print(*arr)