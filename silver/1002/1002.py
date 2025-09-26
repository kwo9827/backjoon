import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue

    dx = x1 - x2
    dy = y1 - y2
    d2 = dx * dx + dy * dy

    sum_r = r1 + r2
    diff_r = abs(r1-r2)
    sum2 = sum_r * sum_r
    diff2 = diff_r * diff_r

    if d2 > sum2:
        print(0)
    elif d2 < diff2:
        print(0)
    elif d2 == sum2:
        print(1)
    elif d2 == diff2:
        print(1)
    else:
        print(2)