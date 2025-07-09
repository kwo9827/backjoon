import sys
sys.stdin = open('input.txt')

def compress(coords):
    unique = sorted(set(coords))
    mapping = {v: i+1 for i, v in enumerate(unique)}  # 1-based
    return [mapping[x] for x in coords], len(unique)

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)

    def update(self, i, value):
        while i < len(self.tree):
            self.tree[i] += value
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

T = int(input())
for _ in range(T):
    n = int(input())
    islands = []
    y_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        islands.append((x, y))
        y_list.append(y)

    # 압축
    compressed_y, size = compress(y_list)
    for i in range(n):
        islands[i] = (islands[i][0], compressed_y[i])

    # x 오름차순, y 내림차순 정렬
    islands.sort(key=lambda p: (p[0], -p[1]))

    # BIT 초기화
    bit = FenwickTree(size)
    result = 0

    for x, y in islands:
        result += bit.query(y)
        bit.update(y, 1)

    print(result)
