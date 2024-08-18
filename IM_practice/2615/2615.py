# 오목 판정
import sys
sys.stdin = open('input.txt')

arr = [list(map(int,input().split())) for _ in range(19)]

dr1 = [0,1,1]  # 우,우하,아래
dc1 = [1,1,0]

dr2 = [0]
dc2 = [-1]
winner = 0

for r in range(19):
    for c in range(19):
        for i in range(5): # 최대 5개
            cont = 0

            for k in range(3): # 3방향
                nr1 = r + dr1[k] * i
                nc1 = c + dc1[k] * i
                if 0 <= nr1 < 19 and 0<= nc1 < 19 and arr[nr1][nc1] == '1':
                    cont += 1
                    if cont > 5:
                        break

                    if cont == 5:
                        ans_x = nr1
                        ans_y = nc1
                        winner = 1

    print(winner)
    print(ans_x,ans_y)


