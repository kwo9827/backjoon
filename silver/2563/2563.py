import sys
sys.stdin = open('input.txt')

paper = [[0]*100 for _ in range(100)]

N = int(input())

for _ in range(N):
    x, y = map(int,input().split())

    for dx in range(10):
        for dy in range(10):
            paper[y+dy][x+dx] = 1

area = 0
for row in paper:
    area += sum(row)

print(area)