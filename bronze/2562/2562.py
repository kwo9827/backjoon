import sys
sys.stdin = open('input.txt')

max_num = 0
cont = 0

for i in range(9):
    N = int(input())
    if N > max_num:
        max_num = N
        cont = i + 1

print(max_num)
print(cont)