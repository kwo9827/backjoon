import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

path = []
out = []

def dfs(start: int):
    if len(path) == M:
        out.append(' '.join(map(str, path)))
        return
    # 비내림차순 유지: 현재 start 이상만 선택 (같은 수 재사용 허용)
    for num in range(start, N + 1):
        path.append(num)
        dfs(num)        # ★ num 그대로 넘김 → 같은 수 다시 선택 가능
        path.pop()

dfs(1)
print('\n'.join(out))