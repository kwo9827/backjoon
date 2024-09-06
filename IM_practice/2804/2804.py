#2804 크로스워드 만들기
import sys
sys.stdin = open('input.txt')

A, B = map(str,input().split())

arr = [['.'] * len(A) for _ in range(len(B))]

cross_word = ''
for i in range(len(A)):
    if A[i] in B:
        cross_word = A[i]
        A_pos = B.index(cross_word)
        B_pos = i
        break

for r in range(len(B)):
    arr[r][B_pos] = B[r]

for c in range(len(A)):
    arr[A_pos][c] = A[c]

for row in arr:
    print(''.join(row))

