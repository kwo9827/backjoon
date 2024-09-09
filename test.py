from collections import deque

def BFS(start_x, start_y):
    global N, M, arr

    # 상하좌우 이동을 위한 방향 벡터
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    # 방문 확인을 위한 배열과 BFS를 위한 큐
    visited = [[0] * M for _ in range(N)]
    queue = deque([(start_x, start_y, 0)])  # (x 좌표, y 좌표, 거리)
    visited[start_x][start_y] = 1

    max_distance = 0  # 가장 먼 거리를 저장할 변수

    while queue:
        x, y, dist = queue.popleft()
        max_distance = max(max_distance, dist)

        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and not visited[nr][nc]:
                queue.append((nr, nc, dist + 1))
                visited[nr][nc] = 1

    return max_distance

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

max_time = 0  # 육지 두 곳 사이의 최대 시간을 저장할 변수

for r in range(N):
    for c in range(M):
        if arr[r][c] == 'L':  # 육지인 경우에만 BFS 수행
            max_time = max(max_time, BFS(r, c))  # BFS를 통해 가장 먼 거리를 갱신

print(max_time)
