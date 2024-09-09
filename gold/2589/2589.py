# 보물섬
import sys
sys.stdin = open('input.txt')

# def DFS(start_x, start_y):
#     global max_distance, distance, visited, N, M, arr
#
#     dr = [0, -1, 0, 1]
#     dc = [1,0,-1,0]
#
#     stack = [(start_x, start_y, 0)]
#     visited[start_x][start_y] = 1
#
#     while stack:
#         x, y, dist = stack.pop()
#         distance = max(distance, dist)
#
#         for k in range(4):
#             nr = x + dr[k]
#             nc = y + dc[k]
#
#             if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and not visited[nr][nc]:
#                 stack.append((nr, nc, dist + 1))
#                 visited[nr][nc] = 1
#
#     return distance
#
# N,M = map(int, input().split())
# arr = [list(input().strip()) for _ in range(N)]
#
# max_distance = 0
#
# for r in range(N):
#     for c in range(M):  # 시작 위치가 고정되어 있지 않기 때문에 모든 곳을 확인해봐야 한다.
#         if arr[r][c] == 'L':  # 육지인 경우 시작
#             visited = [[0] * M for _ in range(N)]  # 방문 장소
#             distance = 0
#             # 가장 긴 시간이 걸리는 육지 두 곳이라 했으니깐
#             if DFS(r,c) > max_distance:
#                 max_distance = DFS(r,c)
#
# print(max_distance)

# def DFS(start_x,start_y):
#     global end_x,end_y,maze
#     visited = [[0] * 16 for _ in range(16)]
#     visited[start_x][start_y] =1
#     stack = [(start_x,start_y)]
#     result = 0
#     dr = [0,-1,0,1]
#     dc = [1,0,-1,0]
#
#     while stack:
#         x,y = stack.pop()
#
#         if (x,y) == (end_x,end_y):
#             result = 1
#             break
#
#         for k in range(4):
#             nr = x + dr[k]
#             nc = y + dc[k]
#             if 0<= nr < 16 and 0<= nc < 16 and maze[nr][nc] != 1 and not visited[nr][nc]:
#                 stack.append((nr,nc))
#                 visited[nr][nc] = 1
#
#     return result
#
#
# for tc in range(1,11):
#     T = int(input())
#     maze = [list(map(int,input())) for _ in range(16)]
#
#     for i in range(16):
#         for j in range(16):
#             if maze[i][j] == 2:
#                 start_x = i
#                 start_y = j
#
#             elif maze[i][j] == 3:
#                 end_x = i
#                 end_y = i
#
#     print(f'#{tc} {DFS(start_x,start_y)}')


# 보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.
#
#
#
# 예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.
#
#
#
# 보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.
#
# 출력
# 첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.


def DFS(start_x, start_y):
    global max_distance, N, M, arr, visited

    # 상하좌우 이동을 위한 방향 벡터
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    stack = [(start_x, start_y, 0)]
    visited[start_x][start_y] = 1
    max_dist = 0  # 시작점에서 가장 먼 거리

    while stack:
        x, y, dist = stack.pop()
        max_dist = max(max_dist, dist)

        # 상하좌우로 이동
        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = 1
                stack.append((nr, nc, dist + 1))

    return max_dist

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

max_distance = 0  # 최장 거리를 저장할 변수

for r in range(N):
    for c in range(M):
        if arr[r][c] == 'L':  # 육지인 경우에만 DFS 수행
            visited = [[0] * M for _ in range(N)]  # 새로운 DFS 탐색마다 방문 배열 초기화
            max_distance = max(max_distance, DFS(r, c))  # 각 육지에서의 최장 거리 갱신

print(max_distance)
