import sys
sys.stdin = open('input.txt')

A, B = map(int,input().split())
C = int(input())

M = B + C

if M >= 60:
    H = A + M//60
    M -= 60 * (M//60)

    if H >= 24:
        H -= 24
else:
    H = A

print(H, M)
