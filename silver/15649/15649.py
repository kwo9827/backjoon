import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

used = [False] * (N+1)
path = []
out = []

def dfs():
    if len(path) == M:
        out.append(' '.join(map(str,path)))
        return

    for num in range(1,N+1):
        if not used[num]:
            used[num] = True
            path.append(num)
            dfs()
            path.pop()
            used[num] = False

dfs()
print('\n'.join(out))