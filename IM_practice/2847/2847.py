#2847 게임을 만든 동준이
import sys
sys.stdin = open('input.txt')

lst = []
N = int(input())
for _ in range(N):
    A = int(input())
    lst.append(A)

cont = 0
i = len(lst) - 1

while i > 0:
    if lst[i] <= lst[i-1]:
        lst[i-1] -= 1
        cont += 1
    else:
        i -= 1

print(cont)