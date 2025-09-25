import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int,input().split()))
plus, minus, mul, div = map(int,input().split())

MAX = -10**18
MIN = 10**18

def div_toward_zero(a, b):
    if a >= 0:
        return a // b
    else:
        return -((-a) // b)

def dfs(idx, cur, p, m, t, d):
    global MAX, MIN
    if idx == N:
        if cur > MAX:
            MAX = cur
        if cur < MIN:
            MIN = cur
        return

    x = A[idx]

    if p > 0:
        dfs(idx+1, cur+x, p-1, m, t, d)
    if m > 0:
        dfs(idx + 1, cur - x, p, m - 1, t, d)
    if t > 0:
        dfs(idx + 1, cur * x, p, m, t - 1, d)
    if d > 0:
        dfs(idx + 1, div_toward_zero(cur, x), p, m, t, d - 1)

dfs(1, A[0], plus, minus, mul, div)
print(MAX)
print(MIN)