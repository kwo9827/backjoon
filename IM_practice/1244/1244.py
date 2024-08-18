# 스위치 끄고 켜기
import sys
sys.stdin = open('input.txt')

N = int(input())  # 스위치 개수
arr = list(map(int,input().split()))  # 전등 상태
student = int(input())  # 학생 수
for _ in range(student):
    a,b = map(int,input().split()) # a = 성별, b = 학생이 받은 수

    if a == 1:  # 남학생이면
        for i in range(1, N + 1):  # 전등을 돌면서
            if i % b == 0:  # b의 배수인 전등을
                arr[i-1] = 1 - arr[i-1]

    if a == 2:  # 여학생이면
        b -= 1
        arr[b] = 1 - arr[b]
        for i in range(1,N):  # 전등을 돌면서
            if b-i >= 0 and b+i < N and arr[b-i] == arr[b+i]:
                arr[b-i] = 1 - arr[b-i]
                arr[b + i] = 1 - arr[b+i]
            else:
                break

for i in range(N):
    print(arr[i], end=" ")
    if (i + 1) % 20 == 0:  # 20번째 스위치까지 출력한 후 줄 바꿈
        print()


