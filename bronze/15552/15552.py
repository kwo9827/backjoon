import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(A + B) + '\n')