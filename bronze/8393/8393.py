import sys
sys.stdin = open('input.txt')

N = int(input())

ans = (N*(N+1)) // 2

print(ans)