import sys
sys.stdin = open('input.txt')

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# 두 정렬된 배열을 합치는 함수
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        lx, ly = left[i]
        rx, ry = right[j]

        # x가 작으면 왼쪽, x가 같으면 y가 작은 쪽
        if lx < rx or (lx == rx and ly <= ry):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 한쪽 다 쓰고 나머지 남아있으면 그대로 붙이기
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# 병합 정렬 함수
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # 왼쪽 절반 정렬
    right = merge_sort(arr[mid:])  # 오른쪽 절반 정렬

    return merge(left, right)      # 합치기

# 실행
sorted_points = merge_sort(points)

for x, y in sorted_points:
    print(x, y)
