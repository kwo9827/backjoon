import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

path = []
out = []

def dfs():
    if len(path) == M:
        out.append(' '.join(map(str,path)))
        return

    for num in range(1, N+1):
        path.append(num)
        dfs()
        path.pop()

dfs()
print('\n'.join(out))