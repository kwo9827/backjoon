import sys
sys.stdin = open('input.txt')

X = int(input()) # 물건 가격 합
N = int(input()) # 물건 종류

ans = 0

for _ in range(N):
    A, B = map(int,input().split())
    ans += A * B

if ans == X:
    print("Yes")
else:
    print("No")