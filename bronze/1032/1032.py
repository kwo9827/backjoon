import sys
sys.stdin = open('input.txt')

N = int(input())
names = [input().strip() for _ in range(N)]

L = len(names[0])
pattern = []

for i in range(L):
    ch = names[0][i]
    ok = True

    for j in range(1,N):
        if names[j][i] != ch:
            ok = False
            break
    pattern.append(ch if ok else '?')

print(''.join(pattern))