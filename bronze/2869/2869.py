import sys
sys.stdin = open('input.txt')

A, B, V = map(int,input().split())

remain = V - A  # 마지막 날까지 오를 수 있는 양
per_day = A - B  # 하루에 올라갈 수 있는 양

day = remain // per_day

if remain % per_day != 0:
    day += 1

day += 1

print(day)