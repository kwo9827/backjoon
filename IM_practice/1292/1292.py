# 1292 쉽게 푸는 문제
import sys
sys.stdin = open('input.txt')

A, B = map(int,input().split())

sum_val = 0

lst = []
for i in range(B):
    lst += [i+1] * (i+1)

for i in range(A-1,B):
    sum_val += lst[i]

print(sum_val)