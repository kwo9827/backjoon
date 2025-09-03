import sys
sys.stdin = open('input.txt')

N = int(input())
M = list(map(int,input().split()))

max_num = max(M)

for i in range(N):
    M[i] = M[i]/max_num*100

print(sum(M)/N)

