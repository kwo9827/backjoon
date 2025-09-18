import sys
sys.stdin = open('input.txt')

N = int(input())

F0  = 0
F1 = 1

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    cont = 2
    while cont <= N:
        Fn = F0 + F1
        F0 = F1
        F1 = Fn
        cont += 1
    print(F1)