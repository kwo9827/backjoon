import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split()))
M = int(input())
for _ in range(M):
    man, number = map(int,input().split())
    if man == 1:
        for i in range(1,len(arr)+1):
            if i % number == 0:
                arr[i-1] = 1 - arr[i-1]

    else:
        number -= 1
        arr[number] = 1 - arr[number]

        for i in range(1,N):
            left = number - i
            right = number + i
            if left >= 0 and right < N:
                if arr[left] == arr[right]:
                    arr[left] = 1 - arr[left]
                    arr[right] = 1 - arr[right]

                else:
                    break

for i in range(N):
    print(arr[i], end=" ")
    if (i + 1) % 20 == 0:  # 20번째 스위치까지 출력한 후 줄 바꿈
        print()