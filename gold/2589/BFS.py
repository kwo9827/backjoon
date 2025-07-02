import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(start_x,start_y):
    global arr, N, M, visited

    dr = [1,0,-1,0]
    dc = [0,1,0,-1]

    queue = deque([(start_x,start_y,0)])
    visited[start_x][start_y] = 1

    max_distance = 0

    while queue:
        x, y, dist = queue.popleft()

        if dist > max_distance:
            max_distance = dist

        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]

            if 0<= nr < N and 0<= nc < M and arr[nr][nc] == 'L' and not visited[nr][nc]:
                queue.append((nr,nc,dist+1))
                visited[nr][nc] = 1

    return max_distance

N, M = map(int,input().split())
arr = [list(map(str,input())) for _ in range(N)]

max_val = 0

for r in range(N):
    for c in range(M):
        if arr[r][c] == 'L':
            visited = [[0] * M for _ in range(N)]
            max_val = max(max_val,BFS(r,c))

print(max_val)


